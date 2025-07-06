from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from app.database.base import Base
from app.models.users import User



# Database URL
DATABASE_URL = "sqlite:///C:/Users/owena/OneDrive/Contract Business June 2025 Build/gov_contracts.db"

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database session setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Reusable function to create a user
def create_user(email, password, company_id):
    hashed_password = pwd_context.hash(password)
    user = User(email=email, hashed_password=hashed_password, company_id=company_id)
    db.add(user)
    print(f"User {email} created for company ID {company_id}")

# Example: Create test users
create_user("northern@test.com", "TestPass123", 1)  # Northern Elevator Ltd
create_user("mitie@test.com", "TestPass123", 2)     # Mitie Group PLC

# Example: Add new clients later like this
# create_user("newclient@test.com", "StrongPassword123", 3)

# Commit changes
db.commit()
db.close()
print("Test users added successfully.")
