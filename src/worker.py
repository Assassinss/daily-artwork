from apscheduler.schedulers.tornado import TornadoScheduler

from src.api import Api

scheduler = TornadoScheduler()
api = Api()


def fetch_photo():
    api.fetch_photo()


def scheduler_worker():
    scheduler.add_job(fetch_photo, 'cron', day='1-31', hour=0, minute=0)
    scheduler.start()
