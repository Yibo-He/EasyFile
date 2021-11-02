# This is a sample Python script.

import os
import shutil
import sys
import xml.dom.minidom
import zipfile

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import docx

from .replace import replace

import json
from .myfont import RepStr
from .myfont import Font
import xml.dom.minidom


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')


def get_default(filename):
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse("./" + filename + "/word/theme/theme1.xml")
    collection = DOMTree.documentElement
    # 在集合中获取所有电影
    minorFont = collection.getElementsByTagName("a:minorFont")
    name = minorFont[0].getElementsByTagName("a:latin")[0].getAttribute("typeface")
    return Font(name=name, color="000000", size=10.5)


def process(document,requirements):
    # configf = open(configfile, encoding='utf-8')
    # config = json.load(configf)
    # configf.close()
    # if len(sys.argv) > 1:
    #     config = sys.argv[1]
    config = requirements
    filename = "temp_work"
    document.save(filename+".docx")
    shutil.copyfile(filename + '.docx', filename + '.zip')
    unzip_file(filename + '.zip', filename)
    old = RepStr(str=config["src_str"], name=config["src_typeface"], size=config["src_size"], color=config["src_color"])
    new = RepStr(str=config["dst_str"], name=config["dst_typeface"], size=config["dst_size"], color=config["dst_color"])
    # document = docx.Document(filename + ".docx")
    default = get_default(filename)
    replace(document, default, old, new)
    # document.save("new.docx")
    os.remove(filename + '.zip')
    os.remove(filename+'.docx')
    shutil.rmtree(filename)
    return document



