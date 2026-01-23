#No lo importe porque me da un error y no pude solucionarlo
lista_productos = ["manzana", "banana", "naranja", "pera", "uva"]

print("Ordenados alfabeticamente")
lista_productos.sort()
print(lista_productos, '\n')

print("Ahora eliminamos el segundo producto y mostramos la lista")
lista_productos.pop(1)
print(lista_productos)