from clases.vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def __init__(self, tipo, matricula, marca, modelo, costo_base, capacidad_carga):
        super().__init__(tipo, matricula, marca, modelo, costo_base)
        self.capacidad_carga = capacidad_carga
    
    def costo_mantenimiento(self):
        costo_mantenimiento = self.costo_base
        if self.capacidad_carga > 1000:
            costo_mantenimiento = self.costo_base * 1.15
        return costo_mantenimiento 