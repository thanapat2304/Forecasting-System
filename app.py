from flask import Flask, render_template, request, redirect, url_for, flash, session, abort, jsonify, send_from_directory
from backend.login_funtions import login_route , login_required
from datetime import datetime, timedelta
from backend.product import import_product
from backend.customer import import_customer

app = Flask(__name__)
app.secret_key = '86679f9154d781668b739b1fc8134674'
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route('/login', methods=['GET', 'POST'])
def login():
    current_user = 'admin'
    if request.method == 'POST':
        return login_route()
    return render_template('login.html', current_user=current_user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/', methods=['GET', 'POST'])
def index():
    current_user = 'admin'
    return render_template('login.html', current_user=current_user)

@app.route('/product', methods=['GET', 'POST'])
def product():
    return import_product()

@app.route('/customer', methods=['GET', 'POST'])
def customer():
    return import_customer()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)