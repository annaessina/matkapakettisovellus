from app import app
import users
from flask import render_template, request, redirect

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return render_template('index2.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/destinations')
def destinations():
        return render_template('destinations.html')
#       result = db.session.execute("SELECT destination FROM destinations")
#       destinations = result.fetchall()
#        return render_template("destinations.html", count=len(destinations) destinations=destinations)
#        return render_template("destinations.html")
