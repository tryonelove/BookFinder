import os
basedir = os.path.abspath(os.path.dirname(__file__))

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'BookFinder',
    'host': '172.24.0.3', # DOCKER CONTAINER IP (TO CHANGE!!!)
    'port': '5432',
}


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(12)
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


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
