from apscheduler.schedulers.background import BackgroundScheduler
from app.services.email_service import notify_companies

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(notify_companies, "interval", weeks=1)
    scheduler.start()
