import os

from flask_script import Manager, Shell

from src import create_app
from src.models import Artwork


app = create_app(os.getenv('APP_ENVIRONMENT', 'dev'))
manager = Manager(app)


def make_shell_context():
    return dict(app=app, artwork=Artwork)


manager.add_command('shell', Shell(make_shell_context()))


if __name__ == '__main__':
    manager.run()
