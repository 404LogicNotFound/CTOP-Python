#Crea una función que calcule la media aritmética de dos valores numéricos
#introducidos por el usuario. Asegúrate de que los tipos de datos introducidos son
#correctos (validación de datos de entrada)
def calcular_media():
    while True:
        try:
            num1 = float(input("Introduce el primer valor numérico: "))
            num2 = float(input("Introduce el segundo valor numérico: "))
            break
        except ValueError:
            print("Error: Por favor, introduce valores numéricos válidos.")

    media = (num1 + num2) / 2
    return media
resultado = calcular_media()
print(f"La media aritmética de los dos valores es: {resultado}")
#Ahora crea una versión de la misma función, pero que admita un número variable
#de argumentos, que calcule la media de dos o más valores numéricos.
print("-------------------------------")
def calcular_media_varios(*args):
    if len(args) < 2:
        print("Error: Debes introducir al menos dos valores numéricos.")
        return None

    media = sum(args) / len(args)
    return media
resultado_varios = calcular_media_varios(10, 20, 30, 40)
print(resultado_varios)