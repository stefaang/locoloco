"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restplus import Resource, Namespace
from flask_security import login_required
from . import api_rest
import random

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [login_required]


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

@api_rest.route('/racer/<string:resource_id>')
class Racer(Resource):
    """Racer entity"""

    def get(self, resource_id):
        color = random.choice(['red', 'blue', 'orange'])
        return {'id': resource_id, 'lng': 3.735+0.001*random.random(), 'lat': 51.015+0.0007*random.random(), 'color': color}

@api_rest.route('/marker')
class Racer(Resource):
    """Racer entity"""

    def get(self):
        # TODO
        return [{
            'id': f'marker-{i}',
            'lng': 3.735+0.004*random.random(),
            'lat': 51.015+0.002*random.random(),
            'color': ['red', 'blue', 'orange'][i % 3]
            } for i in range(20)]
