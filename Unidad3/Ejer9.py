numero=input("Ingrese el numero para hacer la tabla de multiplicar: ")
if numero.isdigit():
    numero=int(numero)
    print("Tabla de multiplicar del ", numero)
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")
else:
    print("Por favor ingrese un numero valido.")