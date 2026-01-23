# Lista

estudiantes = ['Ana', 'Luis', 'Carlos']

print("Lista inicial de estudiantes:")
print(estudiantes, '\n')

new = input("Agrega un nuevo estudiante: ")
if new.isalpha():
    estudiantes.append(new)
else:
    raise ValueError("El nombre del estudiante debe contener solo letras.")
print(estudiantes, '\n')

print("Eliminando estudiante:")
estudiantes.remove(estudiantes[-1])
print(estudiantes, '\n')

print('Estudiantes ordenados alfabéticamente:')
print(sorted(estudiantes), '\n')

print('Lista final de los estudiantes:')
print(estudiantes)

# Diccionario

calificaciones = {
    'Ana': 9,
    'Luis': 7,
    'Carlos': 8
}
print("Diccionario inicial de calificaciones:")
print(calificaciones, '\n')

new_calif = input("Agrega el nombre del alumno: ")
if new_calif.isalpha():
    nota = input("Agrega la calificación del alumno (0-10): ")
    if nota.isdigit() and 0 <= int(nota) <= 10:
        calificaciones[new_calif] = int(nota)
    else:
        raise ValueError("La calificación debe ser un número entre 0 y 10.")
else:
    raise ValueError("El nombre del alumno debe contener solo letras.")
print(calificaciones, '\n')

name = input("Consulta la calificación de un estudiante: ")
if name.isalpha():
    print(f"La calificación de {name} es: {calificaciones.get(name, 'Estudiante no encontrado')}", '\n')
else:
    raise ValueError("El nombre del estudiante debe contener solo letras.")

print("La nota media de la clase es:")
total = sum(calificaciones.values())
print(total / len(calificaciones))

#txt
with open('alumnos.txt', 'w') as file:
    for estudiante, calificacion in calificaciones.items():
        file.write(f"{estudiante} - {calificacion}\n")
