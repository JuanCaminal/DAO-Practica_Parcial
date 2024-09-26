from abc import ABC, abstractmethod


class Sucursal(ABC):
    def __init__(self, tipo, id, superficie, facturacion):
        self.tipo = tipo
        self.id = id
        self.superficie = superficie
        self.facturacion = facturacion
       
    def resultado_comercial(self):
        return self.facturacion
    
    def indice_rentabilidad(self):
        return self.resultado_comercial() / self.superficie
    
    def __str__(self):
        return f"Indice rentabilidad: {self.indice_rentabilidad()}"