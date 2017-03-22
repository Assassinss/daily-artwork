from google.appengine.ext import db

from src.utils import today


class Artwork(db.Model):
    date_time = db.StringProperty()
    author = db.StringProperty()
    model = db.StringProperty()
    exposure_time = db.StringProperty()
    aperture = db.StringProperty()
    focal = db.StringProperty()
    iso = db.StringProperty()
    fullUri = db.StringProperty()
    regularUri = db.StringProperty()
    html = db.StringProperty()
    width = db.IntegerProperty()
    height = db.IntegerProperty()

    def save(self, artwork):
        art = Artwork.all().filter('date_time', today()).get()
        print("today: " + today())
        if art is None:
            artwork.put()
            print("save success......")
        else:
            print("Can't insert data to datastore, the datastore already has data")
