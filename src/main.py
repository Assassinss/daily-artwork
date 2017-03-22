from flask import render_template

from src import home
from src.models import Artwork
from src.utils import today, yesterday


@home.route('/')
def home():
    artwork = Artwork.all().filter('date_time', today()).get()
    if artwork is None:
        artwork = Artwork.all().filter('date_time', yesterday()).get()
        if artwork is None:
            return "Hello .... world !!!!!"

    return render_template('home.html', artwork=artwork)
