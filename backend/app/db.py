import click
from flask import current_app, g
from flask.cli import with_appcontext
import pymysql
import datetime

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
                pw varchar(255) not null,
                nickname varchar(255) default 'Anonymous',
                file_cnt int unsigned not null default 0
            )engine=innodb default charset=utf8;
        """
    cursor.execute(sql)
    
    sql = """drop table if exists File"""
    cursor.execute(sql)
    sql = """
        create table File(
                uid varchar(255) not null,
                docId int unsigned not null,
                filename varchar(255) not null,
                processor enum("doc_formatter", "pdf_table_extractor") NOT NULL,
                timestamp DATETIME not null,
                primary key (uid, docId, filename)
            )engine=innodb default charset=utf8;
        """
    cursor.execute(sql)


def create_user(username, passwd, nickname='Anonymous'):
    try:
        db = get_db()
        cursor = db.cursor()
        print(username, passwd, nickname)
        sql = f'insert into User(id, pw, nickname) values("{username}", "{passwd}", "{nickname}")'
        cursor.execute(sql)
        db.commit()
        info = 'OK'
        return True, info
    except:
        return False, "User Already Exists or Unknown Error"

def record_file(file_name, processor):
    splite_fn = file_name.split('-')
    uid = splite_fn[0]
    docId = int(splite_fn[1])
    filename = splite_fn[2]

    db = get_db()
    cursor = db.cursor()
    
    sql = f'''
        insert into File(uid, docId, filename, processor, timestamp) 
            values ("{uid}", "{docId}", "{filename}", "{processor}",
             "{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
        '''
    cursor.execute(sql)
    db.commit()

def get_history_fileList(uid, page_num):
    try:
        db = get_db()
        cursor = db.cursor()
        
        sql = f'select * from File where uid="{uid}" order by timestamp desc'
        cursor.execute(sql)
        data = cursor.fetchall()

        if len(data) == 0:
            return []

        if page_num == 0:
            page_data = data
        elif (page_num - 1) * 10 < len(data):
            page_data = data[(page_num-1)*10 : min(page_num*10, len(data))]
        else:
            return None

        dict_list = [{'path':gen_path(data), 'filename':data[2], 'processor':data[3], 'timestamp':data[4]}\
                for data in page_data]

        return dict_list
    except:
        return None

def gen_path(data):
    return data[0] + '-' + str(data[1]) + '-' + data[2]

def check_password(username, passwd):
    try:
        db = get_db()
        cursor = db.cursor()
        sql = f"select * from User where (id = '{username}' && pw = '{passwd}')"
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res) == 1:
            info = {
                "id": res[0][0],
                "nickname": res[0][2],
                "info": 'OK'
            }
            return 0, info
        else:
            info = {
                "id": None,
                "nickname": None,
                "info": 'Incorrect Username or Password'
            }
            return 1, info
    except:
        info = {
            "id": None,
            "nickname": None,
            "info": "Illegal Input"
        }
        return 1, info
      
def allocate_fileID(uid):
    try:
        db = get_db()
        cursor = db.cursor()

        uid = str(uid)
        sql = f'select * from User where id="{uid}"'
        cursor.execute(sql)

        f = cursor.fetchall()
        cnt = f[0][3]
        print(cnt)

        sql = f'update User set file_cnt="{cnt+1}" where id="{uid}"'
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
