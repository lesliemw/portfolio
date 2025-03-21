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


def write_to_file(data):
    '''This function will write the data to a file'''
    with open("database.txt", mode="a", encoding="utf-8") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email}, {subject}, {message}")


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    '''This function will be called when the form is submitted'''
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect("/thankyou.html")
    else:
        return "something went wrong. Try again"
