# Escribe un que pida al usuario un número del 5 al 12 y muestre su tabla de
# multiplicar (del 1 al 10) usando un bucle for.
try:
    numero = int(input("Introduce un número del 5 al 12: "))
except ValueError:
    print("Error: Por favor, introduce un número entero válido.")
    exit()
if 5 <= numero <= 12:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número fuera de rango. Por favor, introduce un número entre 5 y 12.")
