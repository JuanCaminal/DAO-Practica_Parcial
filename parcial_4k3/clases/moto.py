from clases.vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, tipo, matricula, marca, modelo, costo_base, cc):
        super().__init__(tipo, matricula, marca, modelo, costo_base)
        self.cc = cc
        
    def costo_mantenimiento(self):
        costo_mantenimiento = self.costo_base
        if self.cc > 500:
            costo_mantenimiento = self.costo_base * 1.20
        return costo_mantenimiento 