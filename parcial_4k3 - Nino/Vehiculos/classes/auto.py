from classes.vehiculo import *

class Auto(Vehiculo):
    def __init__(self, tipo, matricula, marca, modelo, costo_base, kilometraje):
        super().__init__(tipo, matricula, marca, modelo, costo_base)
        self.kilometraje = kilometraje

    def costo_total_mantenimiento(self):
        if self.kilometraje > 100000:
            costo_mantenimiento = self.costo_base * 1.10
            return costo_mantenimiento
        else:
            return self.costo_base