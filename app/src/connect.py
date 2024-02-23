import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            conn.autocommit = True
            print('Connected to the PostgreSQL server.')
            if conn == None:
                cursor = conn.cursor()
                sql = ''' CREATE database visiteur_count; '''
                cursor.execute(sql)
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
def Execute_query(conn, query):
    c = conn.cursor()
    res = c.execute(query)
    conn.commit()

def add_one_to_count(conn):
    query = "UPDATE Visiteur_count SET count_usr = count_usr +1;"
    Execute_query(conn, query)

def recreate_database(conn):
    querry = '''
    DROP TABLE IF EXISTS Visiteur_count ;
    DROP TABLE IF EXISTS Visiteur_log ;

CREATE TABLE Visiteur_count (
	count_usr int4 NOT NULL
);

CREATE TABLE Visiteur_log (
	date timestamp NOT NULL,
    ip inet  NULL,
    page varchar(255)  NULL
    
    );
'''
    c = conn.cursor()
    c.execute(querry)
    conn.commit()
    Execute_query(conn, "INSERT INTO Visiteur_count(count_usr) VALUES (0);")

def Execute_mog_query(conn, values, query):
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

def insert_user_log(conn, ip, page):
    #ip = str(ip).replace('.', '-')
    query = f"INSERT INTO Visiteur_log(date, ip, page) VALUES (NOW(), '{ip}', 'page');"
    Execute_query(conn, query)
    
def get_count(conn):
    query = "select count_usr from visiteur_count "
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()[0]

def get_conn():
    config = load_config()
    return connect(config)

if __name__ == '__main__':
    conn = get_conn()
    recreate_database(conn)
    for i in range(10):
        add_one_to_count(conn)
    print(get_count(conn))
    conn.close()