<<<<<<< HEAD
import click
from flask import current_app, g
from flask.cli import with_appcontext
import pymysql

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
 
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

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
        return False, "User Already Exists or Unknown Error"

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
      
def get_user_docID(user_id):
    return 0

def update_docID(user_id, new_docID):
    pass
=======
import click
from flask import current_app, g
from flask.cli import with_appcontext
import pymysql
# from pymysql import cursors

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')
    
def init_db():
    pass

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
    
    sql = """drop table if exists File"""
    cursor.execute(sql)
    sql = """
        create table File(
            id int primary key auto_increment,
            title varchar(255) not null,
            uid varchar(255),
            user_idx int not null
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
        return False, "User Already Exists or Unknown Error"

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
      
def allocate_docID(uid, filename):
    try:
        db = get_db()
        cursor = db.cursor()
        print("uid=", uid)
        uid = str(uid)
        sql = f'select count(*) from File where uid="{uid}"'
        print(sql)
        cursor.execute(sql)
        f = cursor.fetchall()
        print(f)
        cnt = f[0][0]
        print(cnt)
        sql = f'insert into File(title, uid, user_idx) values("{filename}", "{uid}", "{cnt}")'
        cursor.execute(sql)
        db.commit()
        # res = cursor.fetchall()
        info = {
                "idx": cnt,
                "info": 'OK'
        }
        return True, info
    except:
        return False, {"idx": -1, "info": "Unknown Error"}
>>>>>>> 5965d4435a22d5b8f400a221f69aae9c2accfd9e
