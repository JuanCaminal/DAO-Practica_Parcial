from abc import *
class Mantenimiento(ABC):
    
    def __init__(self, tipo, fecha, operario, importe_repuestos):
        self.tipo = tipo
        self.fecha = fecha
        self.operario = operario
        self.importe_repuestos = importe_repuestos
    
    @abstractmethod
    def obtener_costo_mantenimiento(self):
        ...
        
    def es_caro(self):
        return self.obtener_costo_mantenimiento() > 10000