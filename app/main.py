import os
from flask import Blueprint, current_app, send_file

main_bp = Blueprint('main_bp', __name__, url_prefix='/')


@main_bp.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)
