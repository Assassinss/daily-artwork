from flask import render_template

from src import home
from src.models import Artwork
from src.utils import today


@home.route('/')
def home():
    artwork = Artwork.query.filter_by(date_time=today()).first()
    if artwork is not None:
        return render_template('home.html', artwork=artwork)
    else:
        return "Hello .... world !!!!!"
