# Autor: José Manuel Maldonado Martín
# Fecha: 14/11/2025
# Descripción:
# Escribe dos versiones de un programa que calcule la suma de los
# números del 1 al 1.000.000:
# ▪ 1. Usando un bucle for.
# ▪ 2. Usando la función sum(range(...)).


import time
inicio = time.time()
# Versión 1: Usando un bucle for
# Inicializa el acumulador que almacenará la suma calculada por el bucle
suma_for = 0
# Recorre todos los enteros desde 1 hasta 1.000.000 (inclusive)
for i in range(1, 1000001):
    # Añade el valor actual de `i` al acumulador `suma_for`
    suma_for += i
# Muestra el resultado obtenido con el bucle for
print("Suma usando bucle for:", suma_for)
fin = time.time()
print('Tiempo:', fin - inicio, 'segundos')

# Separador visual para distinguir las dos versiones
print("-------------------")

import time
inicio = time.time()
# Versión 2: Usando la función sum(range(...))
# Calcula la suma de 1 a 1.000.000 utilizando la función incorporada `sum`
suma_sum = sum(range(1, 1000001))
# Muestra el resultado obtenido con sum(range(...))
print("Suma usando sum(range(...)):", suma_sum)
fin = time.time()
print('Tiempo:', fin - inicio, 'segundos')
