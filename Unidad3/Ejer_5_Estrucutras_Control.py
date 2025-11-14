edad=input("Introduce la edad: ")
if edad.isdigit():
    edad=int(edad)
    if edad>=65:
        print("Eres mayor")
    elif edad<65 and edad>=18:
        print("Eres adulto")
    elif edad<0:
        print("Es imposible")
    else:
        print("Eres menor")
else:
    print("No has introducido una edad")