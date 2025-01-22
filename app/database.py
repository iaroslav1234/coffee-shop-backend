import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Get database URL from environment variable or use default SQLite URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./coffee_shop.db")

# Handle special case for postgres:// URLs (used by some hosting providers)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Enable automatic reconnection
    pool_size=5,         # Set maximum pool size
    max_overflow=10      # Allow up to 10 connections beyond pool_size
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
