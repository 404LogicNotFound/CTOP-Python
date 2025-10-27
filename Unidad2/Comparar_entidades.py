print("Introduce el primer número :")
num1 = int(input())
print("Introduce el segundo número :")
num2 = int(input())
if num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
elif num2 > num1:
    print(f"El número {num2} es mayor que {num1}")
else:
    print("Ambos números son iguales")
