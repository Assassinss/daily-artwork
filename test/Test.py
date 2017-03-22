import unittest
from src import create_app
import json
import datetime
import os
from src.models import Artwork
from google.appengine.ext import db


class JsonTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app('dev')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_get_id(self):
        self.assertIsNotNone(os.environ['UNSPLASH_APP_ID'])

    def test_today(self):
        today = datetime.date.today()
        formatStr = '%Y%m%d'
        self.assertEqual("20170305", today.strftime(formatStr))

    def test_yesterday(self):
        today_date = datetime.date.today()
        delta_date = datetime.timedelta(days=1)
        yesterday_date = today_date - delta_date
        formatStr = '%Y%m%d'
        self.assertEqual("20170310", yesterday_date.strftime(formatStr))

    def test_gdb(self):
        artwork = Artwork(date_time="20170313", author="Json")
        artwork.put()
