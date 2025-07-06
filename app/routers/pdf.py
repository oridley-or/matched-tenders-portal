from fastapi import APIRouter

router = APIRouter()

@router.get("/pdf/download")
def download_pdf():
    return {"message": "PDF generation not implemented yet."}
