import click
from flask import current_app, g
from flask.cli import with_appcontext

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def get_db():
    # if 'db' not in g:
    #     g.db = sqlite3.connect(
    #         current_app.config['DATABASE'],
    #         detect_types=sqlite3.PARSE_DECLTYPES
    #     )
    #     g.db.row_factory = sqlite3.Row

    # return g.db
    return None

def close_db(e=None):
    pass

def init_db():
    pass

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')