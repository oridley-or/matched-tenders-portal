# app/database/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

from app.database.base import Base

# Use raw string for Windows file path, and convert backslashes to slashes.
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///gov_contracts.db")


engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Add this function:
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Keeps your models connected to Base
def init_db():
    from app.models import users, company, contract, contract_assessments, scope
    Base.metadata.create_all(bind=engine)

