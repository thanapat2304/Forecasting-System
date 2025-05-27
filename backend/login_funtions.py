from flask import session, redirect, url_for, request , make_response, flash
from backend.db_connection import connect_aep_portal

def login_required(f):
    def wrap(*args, **kwargs):
        if 'fda_username' not in session:
            return redirect(url_for('login', error=1))
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap

users = [
    {
        'username': 'admin',
        'password': 'Admin@123',
        'role' : 'admin'
    }
]

def login_route():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return redirect(url_for('index', error="กรุณากรอกข้อมูลให้ครบถ้วน"))

    for user in users:
        if user['username'] == username and user['password'] == password:
            session['fda_username'] = user['username']
            session['fda_role'] = user['role']
            session.permanent = True

            return redirect(url_for('product'))
    else:
        return redirect(url_for('index', error="รหัสผู้ใช้หรือรหัสผ่านไม่ถูกต้อง"))