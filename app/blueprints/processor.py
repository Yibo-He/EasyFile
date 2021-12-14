import os
from flask import (
    Blueprint, g, request, jsonify, send_from_directory, current_app, make_response
)

from ..db import allocate_fileID


bp = Blueprint('processor', __name__)


@bp.route('/upload_file', methods=['POST'])
def upload_doc():
    files_dict = request.files
    
    file_template = {'state': 0, 'info':'success', 'filename':"invalid"}  # to mark the state
    jsondata = []
    error = None
    if files_dict is None:
        error = 'No files uploaded'
        file_info = file_template.copy()
        file_info['state'] = 1
        file_info['info'] = error
        jsondata.append(file_info)
        return jsonify(jsondata)

    if error is None:
        for file_obj in files_dict.values():
            file_info = file_template.copy()
            status, info = allocate_fileID(g.userID)
            if status == True:
                try:
                    docID = info["idx"]
                    print("docid: ", docID)
                    file_name = str(g.userID) + '-' +  str(docID) + '-' + file_obj.filename
                    print("file_name: ", file_name)
                    file_path = os.path.join(current_app.config['TEMP_PATH'], file_name)
                    file_obj.save(file_path)
                    file_info["filename"] = file_name
                except:
                    error = 'Uploading Error' 
                    file_info['state'] = 2
                    file_info['info'] = error
            else:
                error = 'Database Error'
                file_info['state'] = 2
                file_info['info'] = error
            print(file_info)
            jsondata.append(file_info)
    print(jsondata)

    # all the succussfully uploaded files are labeled with state 0
    return jsonify(jsondata)

@bp.route('/download/<filename>', methods=['GET','POST'])
def download(filename):
    filelist = str2list(filename)
    error = check_file_permission(filelist)
    print(error)
    
    if error is None:
        print(current_app.config['STORAGE_PATH'], filename)
        response = make_response(send_from_directory(current_app.config['STORAGE_PATH'], filename, as_attachment=True))
        response.headers["Access-Control-Expose-Headers"] = "Content-disposition"
        return response
    else:
        return jsonify({'state': 1, 'info':error})


def del_temp_files(file_path):
    os.remove(file_path)

def sweep_temp_files():
    pass

def str2list(filename):
    return [filename]

def check_file_permission(file_names):
    print(g.userID)
    for fn in file_names:
        print(fn)
        if str(g.userID) != (fn.split('-'))[0]:
            print(fn.split('-')[0])
            return "Permission denied"

    return None