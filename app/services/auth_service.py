from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.users import User


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ---------------- Password Utilities ----------------
def get_password_hash(password: str) -> str:
    """Hash plain password."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify plain password against hashed."""
    return pwd_context.verify(plain_password, hashed_password)

# ---------------- Authentication Logic ----------------
def authenticate_user(db: Session, email: str, password: str):
    """Check if user exists and password is valid."""
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

# ---------------- Session Helper ----------------
def get_user_by_id(db: Session, user_id: int):
    """Fetch user by ID."""
    return db.query(User).filter(User.id == user_id).first()
