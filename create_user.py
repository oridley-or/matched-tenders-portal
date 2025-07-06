from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from app.database.base import Base
from app.models.users import User


# Database URL
DATABASE_URL = "sqlite:///C:/Users/owena/OneDrive/Contract Business June 2025 Build/gov_contracts.db"

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Setup database connection
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Helper function to create user
def create_user(email, password, company_id):
    hashed_password = pwd_context.hash(password)
    user = User(email=email, hashed_password=hashed_password, company_id=company_id)
    db.add(user)
    print(f"User {email} created for company ID {company_id}")

# Create two test users
create_user("northern@test.com", "TestPass123", 1)  # Northern Elevator Ltd
create_user("mitie@test.com", "TestPass123", 2)     # Mitie Group PLC
#add this to create new users: create_user("newclient@test.com", "StrongPassword123", 3)

# Commit and close session
db.commit()
db.close()
print("Test users added.")
