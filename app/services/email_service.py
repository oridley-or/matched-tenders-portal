import smtplib
from email.mime.text import MIMEText
from app.config import settings

def notify_companies():
    msg = MIMEText("You have X new matched opportunities — click to view.")
    msg["Subject"] = "Weekly Tender Matches"
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = "client@example.com"

    with smtplib.SMTP(settings.SMTP_SERVER) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg)
