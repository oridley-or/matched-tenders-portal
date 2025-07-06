from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    
    # ✅ Fixed table name in ForeignKey
    company_id = Column(Integer, ForeignKey("company.id"), nullable=False)

    company = relationship("Company", back_populates="users")
