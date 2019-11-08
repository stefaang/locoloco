""" API Blueprint Application """

from flask import Blueprint, current_app, redirect, url_for
from flask_restplus import Api
from flask_security import current_user

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api_rest = Api(api_bp)


def public_route(decorated_function):
    decorated_function.is_public = True
    return decorated_function


# @api_bp.before_request
# def check_route_access():
#     if any([request.endpoint.startswith('static/'),
#             current_user.is_authenticated(),  # From Flask-Login
#             getattr(api_bp.view_functions[request.endpoint],'is_public',False)]):
#         return  # Access granted
#     else:
#         return redirect(url_for('users.login_page'))


@api_bp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


# Import resources to ensure view is registered
from .resources import * # NOQA
