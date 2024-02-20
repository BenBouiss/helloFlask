import flask
import jinja2
import sqlite3
import pandas as pd

path = "visits.db"
app = flask.Flask(__name__)


def recreate_database(path):
    query = '''
DROP TABLE IF EXISTS Visiteur ;
CREATE TABLE Visiteur (
	Count int4 NOT NULL
);

    '''
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.executescript(query)
    Execute_query("INSERT INTO Visiteur (Count) VALUES (0);", path)

def Execute_query(query, path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    res = cur.execute(query)
    con.commit()
    con.close()

def Add_one(path):
    query = "UPDATE Visiteur SET Count = Count +1;"
    Execute_query(query, path)

def Get_count(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    query = "SELECT * FROM Visiteur"
    df = pd.read_sql(sql = query, con = con)
    con.close()
    return df.loc[0].values[0]

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
    Add_one(path)
    Count = Get_count(path)
    return flask.render_template("count_1.html", title = "Jinja and Flask", count = Count) 

if __name__ == "__main__":
    Exist = True
    if not Exist:
        recreate_database(path)
    app.run(debug=True)
    
    
