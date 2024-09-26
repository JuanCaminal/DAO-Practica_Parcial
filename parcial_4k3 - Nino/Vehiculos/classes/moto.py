from classes.vehiculo import *


class Moto(Vehiculo):
    def __init__(self, tipo, matricula, marca, modelo, costo_base, cilindrada):
        super().__init__(tipo, matricula, marca, modelo, costo_base)
        self.cilindrada = cilindrada

    def costo_total_mantenimiento(self):
        if self.cilindrada > 500:
            costo_mantenimiento = self.costo_base * 1.20
            return costo_mantenimiento
        else:
            return self.costo_base