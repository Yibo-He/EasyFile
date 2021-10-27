import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.exceptions import abort

from .auth import login_required
from ..db import get_db

bp = Blueprint('doc_formatter', __name__)

@bp.route('/')
def index():
    if g.user is None:
        return {}
    else:
        return g.user

@bp.route('/upload_doc', methods=['POST'])
@login_required
def upload_doc():
    file_obj = request.files['file']
    error = None

    if file_obj is None:
        error = '未上传文件'

    if error is None:
        file_name = str(session.get('user_id')) + '_' +  str(session.get('doc_id')) + '.docx'
        file_path = os.path.join('./temp/', file_name)
        file_obj.save(file_path)

    flash(error)

    return file_path
