import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")
    EMAIL_FROM = os.getenv("EMAIL_FROM")
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")

settings = Settings()
