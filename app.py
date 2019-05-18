import os
import smtplib                                              # simple (e)mail transfer protocol
from flask import Flask, render_template, request, redirect
import csv                              # Comma Separated Value - lightweight database that saves info as a file to my hdd permanently so the data persists

app = Flask(__name__)       # command needed at the top of every Flask application - means turn this file into a web application

# @app.route("/")         #listen now for a GET request to the "/" route
# def index():                    #index is arbitrary, but 'templates' is not
#     # name = request.args.get("name", "User")         # can take a second default value
#     # if not name:                                  # another option to the above solution to allowing user input to change rendering
#     #     name = "User"
#     return render_template("index.html", name=name)                #render_template takes multiple args if you want to dynamically render data
#                        
#                                              # the key 'name' corresponds to the {{ name }} in the index file - if you change 'name' to 'foo', you have to change it in index too


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])                   #must define register route in controller, and ensure it is a post method
def register():
    if not request.form.get("name") or not request.form.get("house"):       # no need for lengthy lines of variables (name = or house = etc.) now, define functions directly
        return render_template("failure.html")
    file = open("registered.csv", "a")                              #a = append - means add a row to the file, so every registration has a new line added
    writer = csv.writer(file)                                   #using 'import csv', you can use a writer to write out ie create files in "(file)" defined on above line
    writer.writerow((request.form.get("name"), request.form.get("house")))          #writerow does what it says - gives you rows/columns using the provided args (technically tuples, hence second set of parentheses) separated by commas
    file.close
    return render_template("registered.html")

@app.route("/registered")
def registered():
    file = open("registered.csv", "r")              # r = read mode
    reader = csv.reader(file)
    students = list(reader)                         # tells python to turn reader into a list
    return render_template("registered.html", students=students)



