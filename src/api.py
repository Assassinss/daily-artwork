import json
import os

import requests
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
        resp = requests.get(url=self.url, headers=self.headers)
        data = json.loads(resp.text)
        if 200 <= resp.status_code < 300:
            artwork = Artwork()
            artwork.date_time = today()
            artwork.created_at = data['created_at']
            artwork.updated_at = data['updated_at']
            user = data['user']
            artwork.author = user['name']
            artwork.photo_id = data['id']
            urls = data['urls']
            artwork.regularUri = urls['regular']
            artwork.fullUri = urls['full']
            exif = data['exif']
            artwork.aperture = exif['aperture']
            artwork.exposure_time = exif['exposure_time']
            artwork.focal = exif['focal_length']
            artwork.model = exif['model']
            artwork.iso = exif['iso']
            artwork.save_to_db(artwork)
        elif resp.status_code >= 300:
            abort(resp.status_code, 'Error processing unspalsh photo.')
