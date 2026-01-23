class Persona:
    def __init__(self, nombre, edad,dni):
        self.nombre = nombre
        self._edad = edad
        self.__dni = dni

p=Persona("Ariel",22,"00000000Z")


def getedad(self):
    return print(self._edad)


print(p.nombre)  # Acceso directo al atributo público
getedad(p) # Acceso al atributo protegido (convención)
print (p.Persona__dni)  # Acceso al atributo privado (name mangling)
