# -*- coding: utf-8 -*-
import pymysql
from flask import Flask, json, request, jsonify
from flask_cors import CORS
from threading import RLock

# connect to database
# db = pymysql.connect(host="127.0.0.1",user="root",password="Cqy59588",database="shopping")
db = pymysql.connect(host="127.0.0.1",user="root",password="sqlmq1016",database="shopping")
cursor = db.cursor()

# start the backend service
app = Flask(__name__)
CORS(app, resources=r'/*')

lock = RLock()


# interfaces
# TODO



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9090)
    db.close()
    print("Good bye!")