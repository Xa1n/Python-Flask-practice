from flask import Flask, render_template, request

app = Flask(__name__)       # command needed at the top of every Flask application - means turn this file into a web application

@app.route("/")         #listen now for a GET request to the "/" route
def index():                    #index is arbitrary
    name = request.args.get("name")
    return render_template("index.html", name=name)                #render_template takes multiple args   