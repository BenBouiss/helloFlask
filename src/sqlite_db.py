import flask
#import jinja2
import sqlite3
import pandas as pd

path = "visits.db"


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
    Execute_query("INSERT INTO Visiteur (Count) VALUES (1);", path)

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

if __name__ == "__main__":
    Exist = True
    if not Exist:
        recreate_database(path)
    
    
