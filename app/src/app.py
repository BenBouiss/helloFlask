#import jinja2
# https://medium.com/@kesaralive/diving-deeper-into-docker-networking-with-docker-compose-737e3b8a3c8c
import flask
from flask import url_for
import sqlite_db
import connect 


db_path = "visits.db"
app = flask.Flask(__name__)

@app.route("/", methods=['GET'])
def main_page():
    Name = "Ben"
    return flask.render_template("index_1.html", title = "Jinja and Flask", name = Name, path = "cat.jpg")

@app.route("/home", methods=["GET"])
def home_fn():
    Name = "Ben"
    return flask.render_template("home_1.html", title = "Jinja and Flask", name = Name)

@app.route("/about", methods=["GET"])
def about():
    return flask.render_template("about_1.html", title = "Jinja and Flask")

@app.route("/form", methods=["GET", "POST"])
def form():
    ip = flask.request.remote_addr
    
    print(flask.jsonify({'ip': flask.request.remote_addr}), 200)
    conn = connect.get_conn()
    connect.insert_user_log(conn, ip, "form")
    conn.close()
    return flask.render_template("form_1.html", title = "Jinja and Flask")

@app.route("/count", methods=["GET"])

def count():
    #count = sqlite_db.Get_count(db_path)
    #sqlite_db.Add_one(db_path)
    con = connect.get_conn()
    count = connect.get_count(con)
    connect.add_one_to_count(con)    
    con.close()
    return flask.render_template("count_1.html", title = "Jinja and Flask", count = count+1) 

if __name__ == "__main__":
    #sqlite_db.recreate_database(db_path)
    con = connect.get_conn()
    exist = True
    if not exit:
        connect.recreate_database(con)
    con.close()
    app.run(debug=False, host='0.0.0.0')