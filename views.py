from app import application
from flask import render_template, url_for, request, redirect, flash, session

@application.route('/')
def index():
    return render_template('home.html')

@application.route('/penjualan')
def penjualan():
    return render_template('kasir_penjualan.html')