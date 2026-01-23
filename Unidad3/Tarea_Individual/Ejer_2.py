# Autor: José Manuel Maldonado Martín
# Fecha: 14/11/2025
# Descripción:
#   Pide un número entero positivo y muestra todos los números desde 1 hasta ese número.
#   Utiliza un bucle for para iterar desde 1 hasta el número incluido.

# Se solicita al usuario que ingrese un número entero positivo y se convierte a entero
num = int(input("Ingrese un número entero positivo: "))

# Se comprueba si el número ingresado es mayor que 0
if num > 0:
    # Si es positivo, se recorre el rango desde 1 hasta num (inclusive)
    for i in range(1, num + 1):
        # Imprime cada número en una nueva línea
        print(i)
else:
    # Si el número no es positivo, muestra un mensaje de error
    print("El número ingresado no es positivo.")