from src import cron

from src.api import Api

api = Api()


def fetch_photo():
    api.fetch_photo()


@cron.route('/worker', methods=['GET'])
def scheduler_worker():
    fetch_photo()
    return 'fetch photo...'
