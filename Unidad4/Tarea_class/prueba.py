Estudiantes = {

    "estudiante1": {

        "nombre": "Ana",

        "apellidos": "Mama lolita",

        "nota": 5

    },

    "estudiante2": {

        "nombre": "Bartolomeo",

        "apellidos": "Lol kapo",

        "nota": 10

    },

    "estudiante3": {

        "nombre": "Michele",

        "apellidos": "Michael Jackson",

        "nota": 9

    },

    "estudiante4": {

        "nombre": "Pedrito",

        "apellidos": "Vaca Lechera",

        "nota": 7

    }

}

for estudiante, datos in Estudiantes.items():
    print(estudiante)
    for clave, valor in datos.items():
        print(" ", clave + ":", valor)
