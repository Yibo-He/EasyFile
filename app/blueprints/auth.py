import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from pymysql import cursors
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app, g
import pymysql
from ..db import create_user, check_password, get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        # error = None
        jsondata = {'state': 0, 'info':'success'}  # to mark the state

        if not username:
            # error = 'Username is required.'
            jsondata['state'] = 1
            jsondata['info'] = 'Username is required'
            return jsonify(jsondata)
        elif not password:
            # error = 'Password is required.'
            jsondata['state'] = 2
            jsondata['info'] = 'Password is required'
            return jsonify(jsondata)
        else:

            result, info = create_user(username, password)
            if not result:
                jsondata['state'] = 3
                jsondata['info'] = info
                

        return jsonify(jsondata)
            # if result:
            #     return redirect(url_for("auth.login"))
            # error = info
        # flash(error)
    # return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("getting username and password", username, password)
        jsondata = {'state': 0, 'info':'success'}  # to mark the state
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
        result, info = check_password(username, password)
        print("result:", result, info)
        if result:
            session.clear()
            session['user_id'] = info['id']
            print("ok")
            # return redirect(url_for('index'))
        else:
            # flash(info['info'])
            jsondata['state'] = 1
            jsondata['info'] = info['info']

    # return render_template('auth/login.html')
    return jsonify(jsondata)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = user_id

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        # if g.user is None:
        #     return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
    
@bp.route('/logout',methods=('GET', 'POST'))
def logout():
    jsondata = {'state': 0, 'info':'success'}  # to mark the state
    session.clear()
    # return redirect(url_for('index'))
    return jsonify(jsondata)