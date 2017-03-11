import os


baseDir = os.path.abspath(os.path.dirname(__file__))


class Config:

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DATABASE_URI = 'sqlite:///' + os.path.join(baseDir, 'dev_artwork.sqlite')


class ProductionConfig(Config):
    # DATABASE_URI = os.environ['DATABASE_URL']
    DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(baseDir, 'artwork.sqlite'))


class TestConfig(Config):
    DATABASE_URI = 'sqlite:///' + os.path.join(baseDir, 'test_artwork.sqlite')


config = {
    'test': TestConfig,
    'production': ProductionConfig,
    'dev': DevConfig
}
