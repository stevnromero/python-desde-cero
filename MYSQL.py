# CREAR UNA CONEXION MYSQL

"""import mysql.connector
conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = " root",
    port = "3306",
    password = ""
)
print(conn.is_connected())"""


#CREAR LA BASE DE DATOS CON MYSQL
"""
import mysql.connector
conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = " root",
    port = "3306",
    password = ""
)
miCursor = conn.cursor()
miCursor.execute("CREATE DATABASE techno")"""


# COMPROBAR SI EXISTE LAS BASES DE DATOS MYSQL

"""import mysql.connector
conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = " root",
    port = "3306",
    password = ""
)
miCursor = conn.cursor()
miCursor.execute("SHOW DATABASES")

for database in miCursor:
    print(f"las bases de datos son: {database}")
"""

# CREAR TABLAS CON MYSQL


