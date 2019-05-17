from flask import Flask, render_template, request

app = Flask(__name__)       # command needed at the top of every Flask application - means turn this file into a web application

# @app.route("/")         #listen now for a GET request to the "/" route
# def index():                    #index is arbitrary, but 'templates' is not
#     # name = request.args.get("name", "User")         # can take a second default value
#     # if not name:                                  # another option to the above solution to allowing user input to change rendering
#     #     name = "User"
#     return render_template("index.html", name=name)                #render_template takes multiple args if you want to dynamically render data
#                        
#                                              # the key 'name' corresponds to the {{ name }} in the index file - if you change 'name' to 'foo', you have to change it in index too

students = []           # basic way to store info before incorporating database

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])                   #must define register route in controller, and ensure it is a post method
def register():
    name = request.form.get("name")                         #getting data from user's form input (as opposed to arguments - because Flask puts get arguments in args and post arguments in forms) and storing in variables
    house = request.form.get("houses")                   
    if not name or not house:                             #then using variables to control for condition where data might not be given before submitting form
        return render_template("failure.html")
    students.append(f"{name} from {house}")            # f strings in python
    return render_template("success.html")                    #now you make a success.html file


