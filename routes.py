from app import app
import users
from flask import render_template, request, redirect

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
