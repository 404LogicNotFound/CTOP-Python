nombre=str(input("Ingrese su nombre: "))
edad=int(input("Ingrese su edad: "))
comprobar_estudiantes= (input("Ingrese su estudiante: "))
estudiante =bool()
if comprobar_estudiantes=="yes":
    estudiante=True
else:
    estudiante=False
print(nombre,edad,estudiante)