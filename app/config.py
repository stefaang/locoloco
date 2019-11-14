"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # If not set fall back to production for safety
    FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'ThisIsVerySecret')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT', 'super-secret-random-salt')

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

    CELERY_CONFIG = {
        'BROKER_URL': os.getenv('CELERY_BROKER', 'redis://'),
        'RESULT_BACKEND': os.getenv('CELERY_BROKER', 'redis://'),
    }

    SOCKETIO_MESSAGE_QUEUE = os.getenv('SOCKETIO_MESSAGE_QUEUE',
                                       os.getenv('CELERY_BROKER', 'redis://'))


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
    CELERY_CONFIG = {
        'BROKER_URL': os.getenv('CELERY_BROKER', 'redis://'),
        'RESULT_BACKEND': os.getenv('CELERY_BROKER', 'redis://'),
        'ALWAYS_EAGER': True,
    }


config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'test': TestingConfig
}
