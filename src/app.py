import jinja2
import flask

app = flask.Flask(__name__)
global count 
count = 0

@app.route("/")
def home():
    Name = "Ben"
    return flask.render_template("index_1.html", title = "Jinja and Flask", name = Name, path = "cat.jpg")

@app.route("/home")
def home_home():
    Name = "Ben"
    return flask.render_template("home_1.html", title = "Jinja and Flask")

@app.route("/about")
def home_about():
    return flask.render_template("about_1.html", title = "Jinja and Flask")

@app.route("/form")
def home_form():
    return flask.render_template("form_1.html", title = "Jinja and Flask")

@app.route("/count")
def home_count():
    global count
    count+=1
    return flask.render_template("count_1.html", title = "Jinja and Flask", count = count) 
if __name__ == "__main__":
    app.run(debug=False)