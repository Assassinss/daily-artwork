from flask import jsonify

from src import artwork
from src.models import Artwork
from src.utils import today, yesterday


@artwork.route('/random', methods=['GET'])
def get_random_photo():
    art = Artwork.query.filter_by(date_time=today()).first()
    if art is None:
        art = Artwork.query.filter_by(date_time=yesterday()).first()
        if art is None:
            data = {'result': None}
            return jsonify(data)

    data = {
        'photo_id': art.photo_id,
        'date_time': art.date_time,
        'author': art.author,
        'model': art.model,
        'exposure_time': art.exposure_time,
        'aperture': art.aperture,
        'focal': art.focal,
        'iso': art.iso,
        'fullUri': art.fullUri,
        'regularUri': art.regularUri
    }

    return jsonify(data)


@artwork.route('/all', methods=['GET'])
def list_all():
    artworks = Artwork.query.all()
    data = []
    for art in artworks:
        data.append({
            'photo_id': art.photo_id,
            'date_time': art.date_time,
            'author': art.author,
            'model': art.model,
            'exposure_time': art.exposure_time,
            'aperture': art.aperture,
            'focal': art.focal,
            'iso': art.iso,
            'fullUri': art.fullUri,
            'regularUri': art.regularUri
        })
    return jsonify(data)
