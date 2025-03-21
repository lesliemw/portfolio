from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def my_home():
    '''This function will render the home page'''
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    '''This function is dynamic and will render the html page of whichever page is requested'''
    return render_template(page_name)


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    '''This function will be called when the form is submitted'''
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect("/thankyou.html")
    else:
        return "something went wrong. Try again"
