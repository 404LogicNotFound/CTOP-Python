class Persona:
    def __init__(self, nombre, edad,dni):
        self.nombre = nombre
        self._edad = edad
        self.__dni = dni

p=Persona("Ariel",22,"00000000Z")

print(p._edad)
print(p.__dni)
