# python
# Autor: José Manuel Maldonado Martín
# Fecha: 14/11/2025
# Descripción:
#   Función que calcula el area de un rectángulo.
#   Se añaden comentarios explicativos sin modificar la lógica original.

def area_rectangulo(base, altura):
    # 'base' y 'altura' se esperan como números (tipo float).
    # El área de un rectángulo se obtiene multiplicando base por altura.
    #El error de los dos ** se cambio por un solo *
    area = base * altura
    # Devolvemos el resultado para que pueda ser usado por quien llame la función.
    return area


# Solicitamos la base al usuario y convertimos la entrada a float para poder operar.
#Pusimos bas en vez de base para no confundir con el nombre del parámetro de la función
bas = float(input('Introduce la base: '))
# Solicitamos la altura al usuario y convertimos la entrada a float para poder operar.
#Pusimos alt en vez de altura para no confundir con el nombre del parámetro de la función
alt = float(input('Introduce la altura: '))
# Calculamos el area usando la función definida y mostramos el resultado por pantalla.
#Quitamos lo de area para imprimir directamente el resultado de la función
print('El área del rectángulo es:', area_rectangulo(bas, alt))