from app import app
import users
from flask import render_template, request, redirect


@app.route("/")
def index():
    return redirect("/home_page")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/index2")
       
        return render_template("error.html", message = "Wrong username or password")

@app.route("/register_normal_user", methods=["GET", "POST"])
def register_normal_user():
    if request.method == "GET":
        return render_template("register_normal_user.html")

    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if len(username) < 1 or len(username) > 15:
            return render_template("error.html", message="Username must have 1-15 characters")

        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")

        if len(password1) < 4:
            return render_template("error.html", message="Password must be at least 4 characters")

        if any(char.isdigit() for char in password1) == False:
            return render_template("error.html", message="Password must contain numbers")

        if users.register(username, password):
            return redirect("/profile")
        else:
            return render_template("error.html", message="Registration failed")

        return redirect("/home_page")




@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/home_page", methods=["GET", "POST"])
def home_page():
    return render_template("home_page.html")


@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/destinations')
def destinations():
    return render_template('destinations.html')
