from src import db


class Artwork(db.Model):
    __tablename__ = 'artwork'
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.String, index=True)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    photo_id = db.Column(db.String)
    author = db.Column(db.String)
    model = db.Column(db.String)
    exposure_time = db.Column(db.String)
    aperture = db.Column(db.String)
    focal = db.Column(db.String)
    iso = db.Column(db.String)
    fullUri = db.Column(db.String)
    regularUri = db.Column(db.String)

    def save_to_db(self, artwork):
        db.session.add(artwork)
        db.session.commit()
        print("save success...")
