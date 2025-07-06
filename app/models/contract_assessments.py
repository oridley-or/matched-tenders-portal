from sqlalchemy import Column, Integer, String, Text, DateTime
from app.database.base import Base

import datetime

class ContractAssessment(Base):
    __tablename__ = "contract_assessments"

    id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, nullable=False)
    company_id = Column(Integer, nullable=False)
    contract_title = Column(String, nullable=False)
    contract_link = Column(String)
    contract_description = Column(Text)
    contract_location = Column(String)
    contract_deadline = Column(String)
    contract_budget = Column(String)
    contract_industry = Column(String)
    verdict = Column(String)
    fit_score = Column(Integer)
    opportunity_type = Column(String)
    analysis_notes = Column(Text)
    evaluated_at = Column(DateTime, default=datetime.datetime.utcnow)
