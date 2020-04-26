from app import app, mysql
from flask import render_template, url_for, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# login wrapper
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please login first')
            return redirect(url_for('login'))
    return wrap


@app.route('/', methods=['POST','GET'])
def login():
    if request.form:
        session.clear()
        uname = request.form['username']
        pwd = request.form['pwd']
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM tuser WHERE userid = '{uname}'")
        data = cur.fetchone()
        cur.close()
        if data:
            if check_password_hash(data['password'], pwd):
                session['logged_in'] = True
                session['username'] = data['userid']
                return redirect(url_for('home'))
            else:
                flash('User ID & Password salah2')
        else:
            flash('User ID & Password salah1')
    elif 'logged_in' in session:
        return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@app.route('/penjualan')
@login_required
def penjualan():
    return render_template('kasir_penjualan.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/admin_add_user')
def admin1():
    userid = 'bimo'
    name = 'Bimo Seto Prakoso'
    password = generate_password_hash('prakoso')
    is_active = 1
    create_date = '2020-04-26'
    is_admin = 1

    qry = f"INSERT INTO tuser VALUES('{userid}', '{name}', '{password}', {is_active}, '{create_date}', {is_admin})"
    cur = mysql.connection.cursor()
    cur.execute(qry)
    mysql.connection.commit()
    cur.close()
    return qry