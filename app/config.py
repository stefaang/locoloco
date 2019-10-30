"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os
from app import app
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # If not set fall back to production for safety
    FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'ThisIsVerySecret')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    if not os.path.exists(DIST_DIR):
        raise Exception(
            'DIST_DIR not found: {}'.format(DIST_DIR))

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    MONGODB_SETTINGS = {
        'db': 'locoloco',
        # 'host': os.environ['MONGODB_URL']
    }
    REDIS_URL = os.getenv('REDIS_URL', '')
    REDIS_CHAN = 'chat'

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER',)
    CELERY_RESULT_BACKEND = os.getenv('CELERY_BROKER',)


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


app.config.from_object('app.config.Config')
