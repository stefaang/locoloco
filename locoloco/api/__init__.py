from flask import Blueprint


# __name__ variable is used to determine root path of the application
api = Blueprint('api', __name__)


# routes separated by resource type, each in own module
from . import views  # noqa
