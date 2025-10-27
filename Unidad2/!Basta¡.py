print("Para salir del bucle, escribe '!Basta¡'")
palabras= []
peticiones=0
while True:
    print("Introduce una palabra:")
    palabra = input()
    if palabra == "!Basta¡":
        print("Has soportado estoicamente", peticiones, "preguntas.")
        break
    else:
        peticiones+=1
    palabras.append(palabra)
    for p in palabras:
        print(p, end=",")

    print("")
