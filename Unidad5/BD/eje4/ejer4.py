import sqlite3

conexion = sqlite3.connect('empresa.db')
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    salario REAL
)
""")
cursor.execute("InSERT INTO empleados (nombre, salario) VALUES (?, ?)", ('Juan Perez', 3000.50))
conexion.commit()

cursor.execute("SELECT * FROM empleados")
empleados = cursor.fetchall()
for empleado in empleados:
    print(empleado)
conexion.close()