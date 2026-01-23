#Importa 2 operaciones del módulo desde otro programa y úsalas.
from operaciones import restar, dividir
resultado_resta = restar(10, 5)
print(f"El resultado de la resta es: {resultado_resta}")
resultado_division = dividir(10, 2)
print(f"El resultado de la división es: {resultado_division}")
