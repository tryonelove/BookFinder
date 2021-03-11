import os
basedir = os.path.abspath(os.path.dirname(__file__))

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'BookFinder',
    'host': 'db',
    'port': '5432',
}


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(12)
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES["user"]}:{POSTGRES["pw"]}@{POSTGRES["host"]}:{POSTGRES["port"]}/{POSTGRES["db"]}'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
