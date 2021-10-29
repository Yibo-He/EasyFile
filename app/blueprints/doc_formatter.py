import os
from ast import literal_eval
from app.tools.formatter import formatter
import docx
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.exceptions import abort

from .auth import login_required
from ..db import get_db, get_user_docID, update_docID
from ..tools.formatter import formatter


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
    files_dict = request.files
    docID = get_user_docID(session.get('user_id'))
    file_names = []
    error = None

    if files_dict is None:
        error = '未上传文件'

    if error is None:
        for file_obj in files_dict.values():
            file_name = str(session.get('user_id')) + '&' +  str(docID) + '&' + file_obj.filename
            file_path = os.path.join('./temp/', file_name)
            try:
                file_obj.save(file_path)
            except:
                error = '文件上传失败: ' + file_obj.filename if error is None else error + ', ' + file_obj.filename

            file_names.append(file_path)
            docID = docID + 1

    flash(error)
    update_docID(session.get('user_id'), docID)

    return jsonify(file_names)


@bp.route('/run_formatter', methods=['POST'])
@login_required
def run_formatter():
    file_names = literal_eval(request.form['file_names'])
    requirements = get_reqs(request.form)
    formatted_names = []

    error = check_file_permission(file_names)

    if error is None:
        for file_name in file_names:
            raw_doc = docx.Document(os.path.join('./temp/', file_name))
            try:
                formatted_doc = formatter(raw_doc, requirements)
            except:
                error = '文件格式转换失败: ' + file_name if error is None else error + ', ' + file_name

            formatted_name = 'formatted_' + file_name
            formatted_doc.save(os.path.join('./temp/', formatted_name))
            formatted_names.append(formatted_name)
        
    flash(error)

    return jsonify(formatted_names)

def check_file_permission(file_names):
    return None
    
def get_reqs(form):
    return [{}, {}]

def del_temp_files(file_paths):
    pass

def sweep_temp_files(user_id):
    pass