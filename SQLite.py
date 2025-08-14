
# creamos una conexion de BD con SQLITE

"""import sqlite3

#establecer conexion
conn = sqlite3.connect("new database.db")

#crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# cerrar la conexion (opcional= al finalizar)
conn.close()
"""


# CREAR BASE DE BATOS SQLITE
"""
import sqlite3 

conn = sqlite3.connect("technology.db")
conn.commit()
conn.close()

def CreateDB():
    conn = sqlite3.connect("technology.db")
    conn.commit()
    conn.close()
CreateDB()"""

# COMPROBAR SI EXISTEN LA BASE DE DATOS SQLITE
"""
import sqlite3
import os

My_database = "technology.db"

if os.path.exists(My_database):
    print(f"la base de datos {My_database} si existe")
    conn = sqlite3.connect(My_database)
else:
    print(f"la base de datos {My_database} no existe")
    conn = sqlite3.connect(My_database)
    conn.close()
    """


