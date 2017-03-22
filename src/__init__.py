from flask import Flask, Blueprint

from config import config

app = Flask(__name__)
artwork = Blueprint('artwork', __name__)
home = Blueprint('home', __name__)
cron = Blueprint('cron', __name__)

from src import views
from src import main
from src import worker


def create_app(config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.register_blueprint(artwork)
    app.register_blueprint(home)
    app.register_blueprint(cron)

    return app
