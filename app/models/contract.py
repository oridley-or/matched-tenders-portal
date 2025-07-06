from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from app.database.base import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    description = Column(Text)
    location = Column(String)
    deadline = Column(String)
    budget = Column(String)
    industry = Column(String)
    scraped_at = Column(DateTime)
    company_id = Column(Integer, ForeignKey("company.id"), nullable=True)
