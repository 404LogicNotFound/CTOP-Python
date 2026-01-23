Stock = {
    "manzana": 4,
    "banana": 2,
    "naranja": 3,
    "pera": 6,
    "uva": 5
}
def total_productos(diccionario):
    total_productos = 0
    for cantidad in diccionario.values():
        total_productos += cantidad
    return total_productos

def listar_productos(diccionario):
    for producto, cantidad in diccionario.items():
       if cantidad >3:
           print(f"{producto}: {cantidad}")

print("Productos con cantidad mayor a 3:")
listar_productos(Stock)
print("Total")
print(total_productos(Stock))