class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

U= Usuario("Ana", 22)

import sqlite3

conexion = sqlite3.connect('usuarios.db')
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, edad INTEGER)")
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (U.nombre, U.edad))

conexion.commit()
print("OK.Base de datos creada")
conexion.close()