# Crea un diccionario que almacene tu nombre, tu edad y si eres estudiante (valor
# booleano), con las claves: "nombre", "edad" y "estudiante".
diccionario = [{
    "nombre": "Ana Gómez",
    "edad": 50,
    "estudiante": False
},
    {
        "nombre": "Luis Martínez",
        "edad": 30,
        "estudiante": True
    },
    {
        "nombre": "Marta Rodríguez",
        "edad": 17,
        "estudiante": False
    }
]
for persona in diccionario:
    if persona['edad'] < 18:
        print(f"El estudiante {persona['nombre']}, con edad, {persona['edad']}, y estudiante,{persona['estudiante']} ,  es menor de edad.")
    elif persona['edad'] >= 18 and persona['edad'] < 25:
        print( f"El estudiante {persona['nombre']}, con edad, {persona['edad']}, y estudiante,{persona['estudiante']} , es muy joven.")
    elif persona['edad'] >= 26 and persona['edad'] < 40:
        print(f"El estudiante {persona['nombre']}, con edad, {persona['edad']}, y estudiante,{persona['estudiante']} , es joven.")
    elif persona['edad'] >= 41:
        print(f"El estudiante {persona['nombre']}, con edad, {persona['edad']}, y estudiante,{persona['estudiante']} , ya no eres joven.")
