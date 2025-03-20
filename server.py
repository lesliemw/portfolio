from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/contact")
def contact_me():
    return render_template("contact.html")


@app.route("/work")
def my_work():
    return render_template("work.html")


@app.route("/works")
def my_works():
    return render_template("works.html")


@app.route("/aboutMe")
def about_me():
    return render_template("about.html")
