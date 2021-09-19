import sqlite3
databaseUrl="./databases/persona.sqlite3"
def cadenaConexion():
    try:
        conn = sqlite3.connect(databaseUrl)
        return conn
    except Exception as ex:
        print ("Error al conectarse a la base sqllite3: ", ex) 