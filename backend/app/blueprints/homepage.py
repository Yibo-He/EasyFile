from flask import (
    Blueprint, g, jsonify,
)

from .auth import login_required
from ..db import get_history_fileList


bp = Blueprint('homepage', __name__,  url_prefix='/homepage')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    return jsonify({'state': 0, 'data':{'userID':g.userID, 'nickname':g.nickname},\
         'info': 'Login required to continue.'})


@bp.route('/history_file/<page_num>', methods=['GET'])
@login_required
def get_history_file(page_num):
    page_num = int(page_num)

    if page_num < 0:
        return jsonify({'state': 1, 'data': None, 'info': 'Page number cannot be negative!'})

    data = get_history_fileList(g.userID, page_num)

    if data is None:
        return jsonify({'state': 2, 'data': None, 'info': 'Page number out of bounds!'})
    else:
        return jsonify({'state': 0, 'data': data, 'info': 'Success!'})