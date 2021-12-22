import os
from flask import Flask
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
    elif isinstance(test_config, str):
        app.config.from_pyfile(test_config, silent=False)
    else:
        app.config.from_mapping(test_config)

    from . import db
    db.init_app(app)

    from .blueprints import auth
    app.register_blueprint(auth.bp)

    from .blueprints import processor
    from .blueprints import doc_formatter
    from .blueprints import pdf_table_extractor
    app.register_blueprint(processor.bp)

    from .blueprints import homepage
    app.register_blueprint(homepage.bp)

    return app
