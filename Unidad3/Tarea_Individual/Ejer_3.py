# python
# Autor: José Manuel Maldonado Martín
# Fecha: 14/11/2025
# Descripción:
#   Pide dos números al usuario y una operación aritmética entre `+`, `-`, `*`, `/`
#   Realiza la operación seleccionada y muestra el resultado.
#   Incluye comprobación de división por cero y manejo de operaciones no válidas.

# Se solicita al usuario el primer número y se convierte a float para permitir
# números decimales. Se usa float en lugar de int para mayor generalidad.
num1 = float(input("Ingrese el primer número: "))

# Se solicita el segundo número y también se convierte a float.
num2 = float(input("Ingrese el segundo número: "))

# Se pide la operación como cadena. Se esperan los caracteres: +, -, *, /
# No se normaliza la entrada (por ejemplo espacios), por lo que el usuario debe
# introducir exactamente uno de esos símbolos.
operacion = input("Ingrese la operación (+, -, *, /): ")

# Se comprueba cuál es la operación solicitada y se calcula el resultado.
if operacion == "+":
    # Suma: se suman num1 y num2
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "-":
    # Resta: num1 menos num2
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "*":
    # Multiplicación: num1 por num2
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "/":
    # División: comprobar división por cero antes de operar
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        # Mensaje de error para evitar excepción por división entre cero
        print("Error: No se puede dividir entre cero.")
else:
    # Si la operación no es ninguna de las anteriores, se informa al usuario.
    print("Operación no válida.")
