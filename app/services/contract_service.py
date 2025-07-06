from sqlalchemy.orm import Session
from app.models.contract_assessments import ContractAssessment
import re

def parse_budget(budget_str: str) -> int:
    """
    Convert budget strings like '£75,000,000' or 'Not specified' to an integer value.
    Non-numeric or unspecified budgets return 0 for filtering purposes.
    """
    if not budget_str or "not specified" in budget_str.lower():
        return 0
    numbers = re.sub(r"[^\d]", "", budget_str)
    return int(numbers) if numbers else 0

def get_filtered_contracts(db: Session, company_id: int, min_budget: int = 0, keyword: str = "", 
                           page: int = 1, page_size: int = 10, hide_zero: bool = False):
    """
    Fetch filtered contracts:
    - By company_id
    - Filter budgets greater than or equal to min_budget
    - Keyword search across title, location, AI notes
    - Optionally hide £0 budget contracts
    - Sorted by fit_score descending
    - Paginated
    """
    query = db.query(ContractAssessment).filter(ContractAssessment.company_id == company_id)

    contracts = query.all()

    # Process filtering in Python to handle budget strings
    filtered = []
    for contract in contracts:
        budget_value = parse_budget(contract.contract_budget)
        
        if budget_value < min_budget:
            continue
        if hide_zero and budget_value == 0:
            continue

        if keyword:
            combined_text = f"{contract.contract_title} {contract.contract_location} {contract.analysis_notes}".lower()
            if keyword.lower() not in combined_text:
                continue

        filtered.append(contract)

    # Sort by fit_score descending
    filtered.sort(key=lambda c: c.fit_score or 0, reverse=True)

    total = len(filtered)

    # Pagination
    start = (page - 1) * page_size
    end = start + page_size
    paginated = filtered[start:end]

    return paginated, total
