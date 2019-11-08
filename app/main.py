import os
from flask import Blueprint, current_app, send_file, request, session, redirect, url_for
from flask_security import login_required


main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
@login_required
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)
