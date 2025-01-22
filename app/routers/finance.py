from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, timedelta
from .. import models, schemas, crud
from ..database import get_db
from ..auth import get_current_user

router = APIRouter()

@router.get("/summary")
async def get_financial_summary(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    try:
        # Convert string dates to datetime objects
        end_date_dt = datetime.fromisoformat(end_date.replace('Z', '+00:00')) if end_date else datetime.utcnow()
        
        if start_date:
            start_date_dt = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
        else:
            # If no start date provided, use the beginning of the day
            start_date_dt = end_date_dt.replace(hour=0, minute=0, second=0, microsecond=0)

        # Get all orders between start_date and end_date
        orders = crud.get_orders_by_date_range(db, start_date_dt, end_date_dt)

        # Calculate totals
        total_revenue = sum(order.total_amount for order in orders)
        total_cost = sum(
            sum(item.quantity * item.menu_item.cost_price for item in order.order_items)
            for order in orders
        )
        total_profit = total_revenue - total_cost

        # Prepare hourly data for the chart
        hourly_data = []
        current = start_date_dt
        while current <= end_date_dt:
            hour_end = current + timedelta(hours=1)
            hour_orders = [
                order for order in orders
                if current <= order.created_at < hour_end
            ]
            
            hour_revenue = sum(order.total_amount for order in hour_orders)
            hour_cost = sum(
                sum(item.quantity * item.menu_item.cost_price for item in order.order_items)
                for order in hour_orders
            )
            
            hourly_data.append({
                "time": current.strftime("%H:%M"),
                "revenue": hour_revenue,
                "cost": hour_cost,
                "profit": hour_revenue - hour_cost
            })
            
            current = hour_end

        return {
            "total_revenue": total_revenue,
            "total_cost": total_cost,
            "total_profit": total_profit,
            "data": hourly_data
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
