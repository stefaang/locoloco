import os
from flask import Flask, current_app, send_file, url_for

from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO
from flask_security import Security, MongoEngineUserDatastore
from celery import Celery

from .config import config

# Flask extensions
db = MongoEngine()
socketio = SocketIO()

from app.models.user import User, Role
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security()

celery = Celery(__name__,
                broker=os.environ.get('CELERY_BROKER_URL', 'redis://'),
                backend=os.environ.get('CELERY_BROKER_URL', 'redis://'))
celery.config_from_object('celeryconfig')


def create_app(config_name=None, main=True):
    if config_name is None:
        config_name = os.getenv('LOCOLOCO_CONFIG', 'dev')
    app = Flask(__name__, static_folder='../vuetest/derp/dist')
    app.config.from_object(config[config_name])

    # Initialize flask extensions
    db.init_app(app)
    security.init_app(app, user_datastore)

    # Create a user to test with
    @app.before_first_request
    def create_user():
        user_datastore.create_user(email='stefaang@gmail.com', password='password')

    if main:
        # Initialize socketio server and attach it to the message queue, so
        # that everything works even when there are multiple servers or
        # additional processes such as Celery workers wanting to access
        # Socket.IO
        socketio.init_app(app,
                          message_queue=app.config['SOCKETIO_MESSAGE_QUEUE'])
    else:
        # Initialize socketio to emit events through through the message queue
        # Note that since Celery does not use eventlet, we have to be explicit
        # in setting the async mode to not use it.
        socketio.init_app(None,
                          message_queue=app.config['SOCKETIO_MESSAGE_QUEUE'],
                          async_mode='threading')
    celery.conf.update(config[config_name].CELERY_CONFIG)

    # Register web application routes
    from .main import main_bp
    app.register_blueprint(main_bp)

    # Register API routes
    from .api import api_bp
    # from .client import client_bp
    app.register_blueprint(api_bp)
    # app.register_blueprint(client_bp)

    # Register async tasks support
    #TODO

    app.logger.info('>>> {}'.format(config[config_name].FLASK_ENV))

    return app



