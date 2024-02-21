#import jinja2
import flask
from flask import url_for

app = flask.Flask(__name__)
global count 
count = 0

@app.route("/", methods=['GET'])
def main_page():
    Name = "Ben"
    return flask.render_template("index_1.html", title = "Jinja and Flask", name = Name, path = "cat.jpg")

@app.route("/home")
def home_fn():
    Name = "Ben"
    return flask.render_template("home_1.html", title = "Jinja and Flask", name = Name)

@app.route("/about")
def about():
    return flask.render_template("about_1.html", title = "Jinja and Flask")

@app.route("/form")
def form():
    return flask.render_template("form_1.html", title = "Jinja and Flask")

@app.route("/count")
def count():
    global count
    count+=1
    return flask.render_template("count_1.html", title = "Jinja and Flask", count = count) 
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')