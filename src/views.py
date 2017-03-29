from flask import jsonify

from src import artwork
from src.models import Artwork
from src.utils import today, yesterday


def create_data(art):
    return {
        'date_time': art.date_time,
        'author': art.author,
        'model': art.model,
        'width': art.width,
        'height': art.height,
        'exposure_time': art.exposure_time,
        'aperture': art.aperture,
        'focal': art.focal,
        'iso': art.iso,
        'fullUri': art.fullUri,
        'regularUri': art.regularUri,
        'html': art.html
    }


@artwork.route('/photo', methods=['GET'])
def photo():
    art = Artwork.all().filter('date_time', today()).get()
    if art is None:
        art = Artwork.all().filter('date_time', yesterday()).get()
        if art is None:
            data = {'result': None}
            return jsonify(data)

    data = create_data(art)

    return jsonify(data)


@artwork.route('/photos/all', methods=['GET'])
def list_all():
    artworks = Artwork.all()
    data = []
    for art in artworks:
        data.append({
            'date_time': art.date_time,
            'author': art.author,
            'model': art.model,
            'width': art.width,
            'height': art.height,
            'exposure_time': art.exposure_time,
            'aperture': art.aperture,
            'focal': art.focal,
            'iso': art.iso,
            'fullUri': art.fullUri,
             'regularUri': art.regularUri,
            'html': art.html
        })
    return jsonify(data)


@artwork.route("/photos/page/<int:page>", methods=['GET'])
def get_page_data(page):
    offset = (page - 1) * 20
    artworks = Artwork.all().fetch(limit=20, offset=offset)
    data = []
    for art in artworks:
        data.append({
            'date_time': art.date_time,
            'author': art.author,
            'model': art.model,
            'width': art.width,
            'height': art.height,
            'exposure_time': art.exposure_time,
            'aperture': art.aperture,
            'focal': art.focal,
            'iso': art.iso,
            'fullUri': art.fullUri,
            'regularUri': art.regularUri,
            'html': art.html
        })
    if len(data) == 0:
        data = [{
            'result': None
        }]

    return jsonify(data)
