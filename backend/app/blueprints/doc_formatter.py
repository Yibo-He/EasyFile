import os
import docx
from flask import (
    g, request, jsonify, current_app
)
import ltp  # # this is for debug. Not necessary when it's integrated to formatter.

from .processor import bp, check_file_permission, del_temp_files
from ..tools.formatter import formatter
from ..tools.ner import get_ner  # this is for debug. Not necessary when it's integrated to formatter.
from ..db import record_file
from ..db import my_ltp

@bp.route('/run_formatter', methods=['POST'])
def run_formatter():
    file_names = request.form['file_names'].split(',')
    print(file_names)
    
    requirements = get_reqs(request.form)
    print(requirements)
    
    jsondata = []
    file_template = {'state': 0, 'info':'success', 'formatted_name':"invalid", 'original_name': "invalid"}

    error = check_file_permission(file_names)

    if error is not None:
        file_info = file_template.copy()
        file_info['state'] = 1
        file_info['info'] = error
        jsondata.append(file_info)
        return jsonify(jsondata)
    else:
        for file_name in file_names:
            file_info = file_template.copy()
            file_info['original_name'] = file_name
            try:
                path = os.path.join(current_app.config['TEMP_PATH'], file_name)
                print(path)
                raw_doc = docx.Document(path)
            except docx.opc.exceptions.PackageNotFoundError:  # this is a common error
                error = 'No such file: ' + file_name
                file_info['state'] = 3
                file_info['info'] = error
                jsondata.append(file_info)
                continue
            except:
                error = 'Not Supported: ' + file_name + '. Please make sure the doc file is ended with "docx"'
                file_info['state'] = 3
                file_info['info'] = error
                jsondata.append(file_info)

            try:
                formatted_doc = formatter(raw_doc, requirements, my_ltp)
                # get_ltp calls to load the tagger. The loading takes about 10s. We can do this in the initialization in the future. 

                formatted_name = file_name
                formatted_doc.save(os.path.join(current_app.config['STORAGE_PATH'], formatted_name))
                file_info['formatted_name'] = formatted_name

                record_file(formatted_name, "doc_formatter")
                del_temp_files(path)

            except:
                error = 'failed to transform the file: ' + file_name
                file_info['state'] = 2
                file_info['info'] = error

            jsondata.append(file_info)
            
    print(jsondata)
    return jsonify(jsondata)

# this is for debug. You can try extracting entities in a sentence (in Chinese) with postman.
'''
@bp.route('/ner/<sentence>', methods=['GET','POST'])
def get_entities(sentence):
    if 'myltp' in g:
        print("loading the cached ltp.")
        myltp = g.myltp
    else:
        print("initializing...")
        g.myltp = ltp.LTP()
        myltp = g.myltp
    print("Initialized the ltp.")
    return str(get_ner(sentence, myltp))


def get_ltp():
    # To load the entity tagger. A better way to store it as a global variable is to explore.
    # Note this will cost around 10 seconds!
    if "myltp" not in g:
        g.myltp = ltp.LTP()
    return g.myltp
'''

def get_reqs(form):
    req_dict = {}
    for k,v in form.items():
        if k != 'file_names':
            print("k, v", k, v)
            req_dict[k] = v if k != 'src_size' and k!= 'dst_size' else float(v)
    return [req_dict]