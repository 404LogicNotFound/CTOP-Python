lista_frutas= ["Mango","Banana","Mango","Banana","Manzana"]
print("El primer elemento de la lista es: ", lista_frutas[0])
print("El ultimo elemento de la lista es: ", lista_frutas[-1])
print("El numero total de frutas es:", len(lista_frutas))
print("Ahora añadimos un elemtos nuevo y mostraremos todas las frutas")
lista_frutas.append("Cereza")
for fruta in lista_frutas:
    print(fruta)
