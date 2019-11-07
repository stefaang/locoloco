""" pytests for Flask """

import pytest
from app import create_app


def setup_module():
    app = create_app('test')
    return app.test_client()


def test_api(client):
    resp = client.get('/')
    assert resp.status_code == 200
