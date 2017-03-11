import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from src import create_app
from src import db
from src.models import Artwork


app = create_app(os.getenv('APP_ENVIRONMENT', 'dev'))
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, artwork=Artwork)


manager.add_command('shell', Shell(make_shell_context()))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    config = os.getenv('APP_ENVIRONMENT', 'dev')
    if config == 'dev' or config == 'test':
        manager.run()
    else:
        port = int(os.environ.get('PORT', 5000))
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(port=port, address='0.0.0.0')
        IOLoop.instance().start()
