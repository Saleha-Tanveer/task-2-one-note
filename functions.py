from datetime import timedelta
from functools import wraps

from flask import session, jsonify, app, request
from werkzeug.exceptions import abort

from Schemas.UserModel import User
from database import db
from validators import password_is_valid

"""
    Login required decorator.
    the function checks the session id. if exists, continues the task.
    else returns Login Required.
"""


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:  # check if session exists
            return f(*args, **kwargs)
        else:
            return jsonify("Login required. No active session")
    return wrap


# register route
@app.route('/register/', methods=['POST'])
def registration():
    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or password is None:
        abort(400)  # missing arguments
    if password_is_valid(password) is None:
        abort(400)
    if User.query.filter_by(username=username).first() is not None:
        abort(400)  # existing user

    new_user = User(username, password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)


# login route
@app.route('/login', methods=['GET'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    existing_user = User.query.filter_by(username=username).first()

    if existing_user is not None:
        if existing_user.password == password:
            session['user_id'] = existing_user.id
            session['logged_in'] = True
            app.permanent_session_lifetime = timedelta(minutes=5)
            return jsonify(existing_user)
        else:
            abort(403)  # wrong password
    else:
        abort(400)  # existing user


# logout
@app.route('/logout', methods=['DELETE'])
@login_required
def logout():
    session.pop('logged_in', None)  # end session
    session.pop('user_id', None)  # clear user_id
    return jsonify("logged out. Session closed")
