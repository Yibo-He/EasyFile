import functools
from flask import (
    Blueprint, g, request, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app, g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature, BadData
import time

from .processor  import sweep_temp_files
from ..db import create_user, check_password, get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/')
def index():
    if g.userID is None:
        return {}
    else:
        return g.userID

@bp.route('/register', methods=('GET', 'POST'))
def register():
    #print('line 15')
    #print(session.get('user_id'))
    jsondata = {}
    if request.method == 'POST':
        print(dir(request))
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        # error = None
        jsondata = {'state': 0, 'info':'success'}  # to mark the state

        if not username:
            jsondata['state'] = 1
            jsondata['info'] = 'Username is required'
            return jsonify(jsondata)
        elif not password:
            jsondata['state'] = 2
            jsondata['info'] = 'Password is required'
            return jsonify(jsondata)
        else:
            result, info = create_user(username, password)
            if not result:
                jsondata['state'] = 3
                jsondata['info'] = info
                

    return jsonify(jsondata)

@bp.route('/login', methods=('GET', 'POST'))
def login():

    jsondata = {}

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("getting username and password", username, password)
        
        '''
                    error = None
                    user = db.execute(
                        'SELECT * FROM user WHERE username = ?', (username,)
                    ).fetchone()

                    if user is None:
                        error = 'Incorrect username.'
                    elif not check_password_hash(user['password'], password):
                        error = 'Incorrect password.'

                    if error is None:
                        session.clear()
                        session['user_id'] = user['id']
                        return redirect(url_for('index'))
        '''
        
        state, info = check_password(username, password)
        print("result:", state, info)

        jsondata['state'] = state
        jsondata['info'] = info['info']
        jsondata['tokenInfo'] = gen_token_seq(info['id'])

    return jsonify(jsondata)
    
@bp.route('/logout',methods=('GET', 'POST'))
def logout():
    sweep_temp_files()
    jsondata = {'state': 0, 'info':'success'}  # to mark the state
    return jsonify(jsondata)
    
@bp.before_app_request
def load_logged_in_user():
    if 'Authorization' in request.headers:
        split_token = request.headers['Authorization'].split(' ')
        if len(split_token) == 2 and split_token[0] == 'jwt':
            token = request.headers['Authorization'].split(' ')[1]
        else:
            g.userID = None
            return
    else:
        g.userID = None
        return
    
    validator = validate_token(token)
    if validator['code'] == 200:
        g.userID = validator['userid']
    else:
        g.userID = None


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.userID is None:
            return jsonify({'state': -1, 'info': 'Login required to continue.'})
        return view(*args, **kwargs)

    return wrapped_view

def gen_token_seq(userid):
    if userid is None:
        return None

    secret_key = current_app.config['SECRET_KEY']
    salt = current_app.config['SALT']
    access_token_expires_in = current_app.config['ACCESS_TOKEN_EXPIRES_IN']
    refresh_token_expires_in = current_app.config['REFRESH_TOKEN_EXPIRES_IN']

    access_token_gen = Serializer(secret_key=secret_key, salt=salt, expires_in=access_token_expires_in )
    refresh_token_gen = Serializer(secret_key=secret_key, salt=salt, expires_in=refresh_token_expires_in )
    timtstamp = time.time()
    access_token = access_token_gen.dumps({
        "userid": userid,
        "iat": timtstamp
    })
    refresh_token = refresh_token_gen.dumps({
        "userid": userid,
        "iat": timtstamp
    })

    data = {
        "access_token": str(access_token, 'utf-8'),
        "access_token_expire_in": access_token_expires_in ,
        "refresh_token": str(refresh_token, 'utf-8'),
        "refresh_token_expire_in": refresh_token_expires_in ,
    }

    return data

def validate_token(token):
    s = Serializer(secret_key=current_app.config['SECRET_KEY'], salt=current_app.config['SALT'])

    try:
        data = s.loads(token)
    except SignatureExpired:
        msg = 'toekn expired'
        return {'code': 401, 'error_code': 'auth_01', 'message': msg}
    except BadSignature as e:
        encoded_payload = e.payload
        if encoded_payload is not None:
            try:
                s.load_payload(encoded_payload)
            except BadData:
                msg = 'token tampered'
                return {'code': 401, 'error_code': 'auth_02', 'message': msg}
        msg = 'badSignature of token'
        return {'code': 401, 'error_code': 'auth_03', 'message': msg}
    except:
        msg = 'wrong token with unknown reason'
        return {'code': 401, 'error_code': 'auth_04', 'message': msg}

    if 'userid' not in data:
        msg = 'illegal payload inside'
        return {'code': 401, 'error_code': 'auth_05', 'message': msg}

    msg = 'user(' + str(data['userid']) + ') logged in by token.'
    userid = data['userid']
    return {'code': 200, 'error_code': 'auth_00', 'message': msg, 'userid': userid}