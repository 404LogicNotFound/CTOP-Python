# Cuenta atrás desde un número dado por el usuario entre 5 y 50
import time
print("Dime un número para iniciar la cuenta atrás desde 5 - 50:")
numero = int(input())
if 5 <= numero <= 50:
    for i in range(numero, -1, -1):
        print(i)
        time.sleep(1)
    print("¡BOOOOOOOOMMMM, que tonto!")
else:
    print("Número fuera de rango. Por favor, introduce un número entre 5 y 50.")