almacen={
    "nombre":"Chaquetas El Invierno",
    "precio":89,
    "stock":100,
},{
    "nombre":"Pantalones Verano",
    "precio":59,
    "stock":150,
},{
    "nombre":"Camisas Primavera",
    "precio":39,
    "stock":200,
},{
    "nombre":"Zapatos Otoño",
    "precio":120,
    "stock":80,

}
print("Precio de las chaquetas:", almacen[0]["precio"])
for i in almacen:
    if i["stock"]>100:
        print("Producto con stock mayor a 100:", i["nombre"])

print('\n',"Valor total del inventario de cada producto:")
for i in almacen:
    valor_total=i["precio"]*i["stock"]
    print(f"{i['nombre']}: {valor_total}€")

