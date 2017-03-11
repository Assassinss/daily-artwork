from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

from config import config

app = Flask(__name__)
db = SQLAlchemy(app)
artwork = Blueprint('artwork', __name__)
home = Blueprint('home', __name__)

from src import views
from src import main


def create_app(config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = config[config_name].DATABASE_URI

    db.create_all()

    app.register_blueprint(artwork)
    app.register_blueprint(home)

    from src.worker import scheduler_worker
    scheduler_worker()

    return app
