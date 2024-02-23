import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def Execute_query(conn, query):
    c = conn.cursor()
    res = c.execute(query)
    conn.commit()

def insert_one(conn):
    print('Inserting one')
    for i in range(10):
        Execute_query(conn, "INSERT INTO Visiteur(count_usr) VALUES (1);")

def recreate_database(conn):
    querry = '''
    DROP TABLE IF EXISTS Visiteur ;

CREATE TABLE Visiteur (
	count_usr int4 NOT NULL
);'''
    c = conn.cursor()
    c.execute(querry)
    conn.commit()


if __name__ == '__main__':
    config = load_config()
    conn = connect(config)
    recreate_database(conn)
    insert_one(conn)
    conn.close()