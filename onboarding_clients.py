from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from app.database.base import Base
from app.models.users import User

# ------------------------ Configuration ------------------------

DATABASE_URL = "sqlite:///C:/Users/owena/OneDrive/Contract Business June 2025 Build/gov_contracts.db"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ------------------------ Database Setup ------------------------

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

# ------------------------ Create User Function ------------------------

def create_user(email: str, password: str, company_id: int):
    db = SessionLocal()
    try:
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            print(f"❌ User with email {email} already exists.")
            return

        hashed_password = pwd_context.hash(password)
        user = User(email=email, hashed_password=hashed_password, company_id=company_id)
        db.add(user)
        db.commit()
        print(f"✅ Successfully created user: {email} for company ID: {company_id}")
    except Exception as e:
        db.rollback()
        print(f"⚠️ Error creating user: {e}")
    finally:
        db.close()

# ------------------------ Add New Clients Here ------------------------

# 🔽 Just copy this line for each new client 🔽
create_user("client1@example.com", "SecurePass123", 1)
# create_user("client2@example.com", "AnotherSecurePass456", 2)

