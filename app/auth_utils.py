from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.auth_service import get_user_by_id

def get_current_company(request: Request, db: Session = Depends(get_db)):
    """
    Dependency to fetch the current user's company based on cookie.
    Raises 401 if not authenticated.
    """
    user_id = request.cookies.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_user_by_id(db, int(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="Invalid user")

    if not user.company:
        raise HTTPException(status_code=403, detail="User not linked to a company")

    return user.company
