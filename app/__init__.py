import os
from flask import Flask, blueprints
from flask_cors import CORS

def create_app(test_config = None):

    app = Flask(__name__, instance_relative_config=True)
    CORS(app, supports_credentials=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if test_config is None:
        app.config.from_pyfile('config.py', silent=False)
    else:
        app.config.from_mapping(test_config)

    from . import db
    # print("Trying to initialize db...")
    db.init_app(app)

    from .blueprints import auth
    app.register_blueprint(auth.bp)

    from .blueprints import doc_formatter
    app.register_blueprint(doc_formatter.bp)
    #app.add_url_rule('/', endpoint='index')

    return app
