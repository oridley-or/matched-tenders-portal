import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.database import init_db
from app.routers import auth, dashboard, pdf
from app.background.notifier import start_scheduler

# Load environment variables from .env
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable is not set")

app = FastAPI()

# Add session middleware for cookie-based sessions
app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,
    same_site="lax",  # Helps prevent CSRF
    https_only=True   # Ensures session cookies only sent over HTTPS
)

# Serve static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Initialize database (creates tables if missing)
init_db()

# Register your routers
app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(pdf.router)

# Start background tasks (weekly email alerts)
start_scheduler()
