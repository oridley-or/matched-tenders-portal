from sqlalchemy import Column, Integer, Text, DateTime

from app.database.base import Base


class CompanyScope(Base):
    __tablename__ = "company_scope"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, unique=True)
    in_scope = Column(Text, nullable=False)      # JSON string
    out_of_scope = Column(Text, nullable=False)  # JSON string
    extracted_at = Column(DateTime)
