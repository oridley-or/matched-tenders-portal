# app/routes/dashboard.py

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth_utils import get_current_company
from app.services.contract_service import get_filtered_contracts

import csv
from io import StringIO

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(
    request: Request,
    company = Depends(get_current_company),
    db: Session = Depends(get_db)
):
    if not company:
        return RedirectResponse(url="/login", status_code=303)

    # Extract query parameters with defaults
    min_budget = int(request.query_params.get("min_budget", 0))
    keyword = request.query_params.get("keyword", "")
    page = int(request.query_params.get("page", 1))
    hide_zero = request.query_params.get("hide_zero") == "1"

    # Fetch filtered contracts
    contracts, total = get_filtered_contracts(
        db=db,
        company_id=company.id,
        min_budget=min_budget,
        keyword=keyword,
        page=page,
        page_size=10,
        hide_zero=hide_zero
    )

    total_pages = max((total + 9) // 10, 1)

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "name": company.name,
        "contracts": contracts,
        "min_budget": min_budget,
        "keyword": keyword,
        "page": page,
        "total_pages": total_pages,
        "total": total,
        "hide_zero": hide_zero
    })


@router.get("/export_csv")
def export_csv(
    request: Request,
    company = Depends(get_current_company),
    db: Session = Depends(get_db)
):
    if not company:
        return RedirectResponse(url="/login", status_code=303)

    # Get current filters from request
    min_budget = int(request.query_params.get("min_budget", 0))
    keyword = request.query_params.get("keyword", "")
    hide_zero = request.query_params.get("hide_zero") == "1"

    # Get all (filtered) contracts for export
    contracts, _ = get_filtered_contracts(
        db=db,
        company_id=company.id,
        min_budget=min_budget,
        keyword=keyword,
        page=1,
        page_size=10000,
        hide_zero=hide_zero
    )

    def generate():
        buffer = StringIO()
        writer = csv.writer(buffer)
        writer.writerow([
            "Title", "Link", "Description", "Location", "Deadline",
            "Budget", "Industry", "Verdict", "Fit Score",
            "Opportunity Type", "Analysis Notes", "Evaluated At"
        ])
        for contract in contracts:
            writer.writerow([
                contract.contract_title,
                contract.contract_link,
                contract.contract_description,
                contract.contract_location,
                contract.contract_deadline,
                contract.contract_budget,
                contract.contract_industry,
                contract.verdict,
                contract.fit_score,
                contract.opportunity_type,
                contract.analysis_notes,
                contract.evaluated_at,
            ])
        buffer.seek(0)
        yield buffer.read()

    return StreamingResponse(generate(), media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=matched_contracts.csv"
    })
