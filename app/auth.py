from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import Response
from app.database import SessionLocal
from app.services.auth_service import authenticate_user, get_user_by_id

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# ----------------- DB Dependency -----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------- Login Form -----------------
@router.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# ----------------- Handle Login -----------------
@router.post("/login")
def login(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = authenticate_user(db, email, password)
    if not user:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})
    
    response = RedirectResponse(url="/dashboard", status_code=302)
    # Secure cookie settings - Set secure=True in production for HTTPS
    response.set_cookie(
        key="user_id",
        value=str(user.id),
        httponly=True,
        secure=True,  # Important: only over HTTPS
        samesite="Lax",  # Prevent CSRF attacks, still allows normal navigation
        max_age=3600  # Cookie expires after 1 hour (optional, for added safety)
    )
    return response

# ----------------- Logout -----------------
@router.get("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie(key="user_id")
    return response

# ----------------- Shared Dependency: Get Current User -----------------
def get_current_user(request: Request, db: Session = Depends(get_db)):
    """Returns the logged-in user or raises 401."""
    user_id = request.cookies.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_user_by_id(db, int(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="Invalid user")

    return user
