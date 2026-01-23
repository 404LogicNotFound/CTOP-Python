# Autor: José Manuel Maldonado Martín
# Fecha: 14/11/2025
# Descripción:
#   Solicita tres números enteros al usuario y muestra cuál es el mayor.
#    Usa condicionales múltiples (if\-elif\-else)

# Pide al usuario el primer número y lo convierte a entero
num = int(input("Ingrese un numero: "))

# Pide al usuario el segundo número y lo convierte a entero
num2 = int(input("Ingrese otro numero: "))

# Pide al usuario el tercer número y lo convierte a entero
num3 = int(input("Ingrese un ultimo numero: "))

# Comprueba si el primer número es mayor que los otros dos
if num > num2 and num > num3:
    # Si se cumple, imprime que el primer número es el mayor
    print(f"El numero mayor es: {num}")

# Si no, comprueba si el segundo número es mayor que los otros dos
elif num2 > num and num2 > num3:
    # Si se cumple, imprime que el segundo número es el mayor
    print(f"El numero mayor es: {num2}")

# Si ninguna de las condiciones anteriores se cumple, entra en else
else:
    # Aquí se cubre el caso en que el tercer número sea el mayor
    # Nota: si hay empates (por ejemplo dos números iguales y mayores),
    # este bloque también se ejecutará y mostrará `num3`
    print(f"El numero mayor es: {num3}")
