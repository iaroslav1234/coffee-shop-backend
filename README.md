# Coffee Shop Manager Backend

FastAPI backend for the Coffee Shop Manager application, providing API endpoints for inventory management, sales tracking, and user authentication.

## Features

- User Authentication (JWT)
- Password Reset via Email
- Inventory Management
- Sales Tracking
- Financial Reports
- Email Integration

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- SMTP Email Integration

## Getting Started

### Prerequisites
- Python 3.8 or higher
- PostgreSQL

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/coffee-shop-backend.git
cd coffee-shop-backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Update .env with your configuration
```

5. Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Environment Variables

```env
# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
FROM_EMAIL=your_email@gmail.com
SUPPORT_EMAIL=support@coffeeshop.com

# Frontend URL
FRONTEND_URL=http://localhost:3000

# JWT Secret
SECRET_KEY=your_secret_key
```

## API Documentation

Once the server is running, you can access:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
