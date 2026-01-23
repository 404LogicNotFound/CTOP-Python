#Crea un módulo llamado operaciones.py que contenga las funciones sumar(),
#restar(), multiplicar() y dividir(). Asegúrate de que el módulo no pueda
#ser ejecutado como un programa independiente.
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b
if __name__ == "__main__":
    print("Este módulo no puede ser ejecutado como un programa independiente.")