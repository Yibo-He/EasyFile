import os
from flask import (
    request, jsonify, current_app
)

from .processor import bp, check_file_permission, del_temp_files
from ..tools.pdf import process
from ..db import record_file


@bp.route('/run_pdf2chart', methods=['POST'])
def run_pdf2chart():
    file_names = request.form['file_names'].split(',')
    print(file_names)

    cwd_bak = os.getcwd()
    pages = request.form['src_pages']
    jsondata = []
    file_template = {'state': 0, 'info':'success', 'chart_name':"invalid", 'original_name': "invalid"}

    error = check_file_permission(file_names)

    if error is not None:
        file_info = file_template.copy()
        file_info['state'] = 1
        file_info['info'] = error
        jsondata.append(file_info)
        return jsonify(jsondata)
    else:
        for file_name in file_names:
            try:
                os.mkdir(file_name)
            except Exception as e:
                print(e)
                pass
            file_info = file_template.copy()
            file_info['original_name'] = file_name
            try:
                file_path = os.path.join(current_app.config['TEMP_PATH'], file_name)
                assert os.path.exists(file_path)
                
            except:
                error = 'No such file: ' + file_name
                file_info['state'] = 3
                file_info['info'] = "File not found"
                jsondata.append(file_info)
                continue
            try:
                formatted_name = os.path.splitext(file_name)[0] + '.zip'
                save_path = os.path.join(current_app.config['STORAGE_PATH'], formatted_name)
                os.chdir(os.path.join(cwd_bak, file_name))
                ret = process(file_path,format='excel',ext='xlsx',rules=[pages])
                os.chdir(cwd_bak)
                with open(save_path,'wb') as f:
                    f.write(ret)
                file_info['formatted_name'] = formatted_name

                record_file(formatted_name, "pdf_table_extractor")
                del_temp_files(file_path)
            
            except:
                os.chdir(cwd_bak)
                error = 'failed to transform the file: ' + file_name
                file_info['state'] = 2
                file_info['info'] = error

            try:
                print("rm -R \"%s\"" % file_name)
                os.system("rm -R \"%s\"" % file_name)
            except:
                pass
            jsondata.append(file_info)

    print(jsondata)
    return jsonify(jsondata)