import click
from flask import current_app, g
from flask.cli import with_appcontext
import pymysql

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def get_db():
    if 'db' not in g:
        db_config = current_app.config['DATABASE']
        g.db = pymysql.connect(host=db_config['host'], port=db_config['port'], \
            user=db_config['user'], passwd=db_config['passwd'], db=db_config['db'])

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    # the code below has been checked in mysql.
    print("Initializing db...")
    db = get_db()
    cursor = db.cursor()
    sql = """drop table if exists User"""
    cursor.execute(sql)
    sql = """
        create table User(
            id varchar(255) not null primary key,
            pw varchar(16)
            )engine=innodb default charset=utf8;
        """
    cursor.execute(sql)

def create_user(username, passwd):
    try:
        db = get_db()
        cursor = db.cursor()
        sql = f'insert into User(id, pw) values("{username}", "{passwd}")'
        cursor.execute(sql)
        db.commit()
        info = 'OK'
        return True, info
    except:
        return False, "Unknown Error"

def check_password(username, passwd):
    try:
        db = get_db()
        cursor = db.cursor()
        sql = f"select * from User where (id = '{username}' && pw = '{passwd}')"
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res) > 0:
            info = {
                "id": res[0][0],
                "info": 'OK'
            }
            return True, info
        else:
            info = {
                "id": None,
                "info": 'Incorrect Username or Password'
            }
            return False, info
    except:
        info = {
            "id": None,
            "info": "Illegal Input"
        }
        return False, info

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')