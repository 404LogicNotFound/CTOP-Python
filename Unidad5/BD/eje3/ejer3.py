class Cuenta:
    def __init__(self,saldo):
        self.saldo=saldo

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,cantidad):
        if cantidad >=0:
            self._saldo=cantidad
        else:
            print("El saldo no puede ser negativo")


c=Cuenta(300)
print(c.saldo)

c.saldo=-200
print(c.saldo)