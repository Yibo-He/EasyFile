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
    jsondata = {'state': 0, 'info':'success', 'filenames':[] }  # to mark the state

    file_names = []
    error = None

    if files_dict is None:
        error = '未上传文件'
        jsondata['state'] = 1
        jsondata['info'] = error
        return jsonify(jsondata)

    if error is None:
        for file_obj in files_dict.values():
            file_name = str(session.get('user_id')) + '&' +  str(docID) + '&' + file_obj.filename
            file_path = os.path.join('./temp/', file_name)
            try:
                file_obj.save(file_path)
            except:
                error = '文件上传失败: ' + file_obj.filename if error is None else error + ', ' + file_obj.filename
                jsondata['state'] = 2
                jsondata['info'] = error
            file_names.append(file_path)
            docID = docID + 1
        jsondata['filenames'] = file_names

    # flash(error)
    update_docID(session.get('user_id'), docID)

    # return jsonify(file_names)
    return jsonify(jsondata)


@bp.route('/run_formatter', methods=['POST'])
@login_required
def run_formatter():
    
    file_names = literal_eval(request.form['file_names'])
    requirements = get_reqs(request.form)
    formatted_names = []
    jsondata = {'state': 0, 'info':'success', 'formatted_names':[] }  # to mark the state


    error = check_file_permission(file_names)
    if error is not None:
        jsondata['state'] = 1
        jsondata['info'] = error
        return jsonify(jsondata)

    else:
        for file_name in file_names:
            raw_doc = docx.Document(os.path.join('./temp/', file_name))
            try:
                formatted_doc = formatter(raw_doc, requirements)
                formatted_name = 'formatted_' + file_name
                formatted_doc.save(os.path.join('./temp/', formatted_name))
                formatted_names.append(formatted_name)
            except:
                error = '文件格式转换失败: ' + file_name if error is None else error + ', ' + file_name
                jsondata['state'] = 2
                jsondata['info'] = error

        jsondata['formatted_names'] = formatted_names

    # flash(error)
    # return jsonify(formatted_names)
    return jsonify(jsondata)

def check_file_permission(file_names):
    return None
    
def get_reqs(form):
    # just for test
    return [
        {"src_str":"用户","src_typeface":"等线","src_size":16,"src_color":"000000",
        "dst_str":"我","dst_typeface":"宋体","dst_size":12,"dst_color":"66ccff"},

        {"src_str":"图","src_typeface":"","src_size":0,"src_color":"",
        "dst_str":"我","dst_typeface":"宋体","dst_size":12,"dst_color":"66ccff"}]
    # return [{}, {}]

def del_temp_files(file_paths):
    pass

def sweep_temp_files(user_id):
    pass