import json
import os

from google.appengine.api import urlfetch
from flask import abort

from src.models import Artwork
from src.utils import today


class Api:
    def __init__(self):
        self.url = 'https://api.unsplash.com/photos/random'
        self.headers = {
            'Accept-Version': 'v1',
            'Authorization': 'Client-ID %s' % os.environ['UNSPLASH_APP_ID']
        }

    def fetch_photo(self):
        resp = urlfetch.fetch(url=self.url, headers=self.headers)
        data = json.loads(resp.content)
        if 200 <= resp.status_code < 300:
            artwork = Artwork()
            artwork.date_time = today()
            user = data['user']
            artwork.author = user['name']
            artwork.width = data['width']
            artwork.height = data['height']
            artwork.html = data['links']['html']
            urls = data['urls']
            artwork.regularUri = urls['regular']
            artwork.fullUri = urls['full']
            exif = data['exif']
            artwork.aperture = exif['aperture']
            artwork.exposure_time = exif['exposure_time']
            artwork.focal = exif['focal_length']
            artwork.model = exif['model']
            artwork.iso = str(exif['iso'])
            artwork.save(artwork)
        elif resp.status_code >= 300:
            abort(resp.status_code, 'Error processing unspalsh photo.')
