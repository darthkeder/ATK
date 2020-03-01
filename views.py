from app import app
from flask import render_template, url_for, request, redirect, flash, session

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/penjualan')
def penjualan():
    return render_template('kasir_penjualan.html')