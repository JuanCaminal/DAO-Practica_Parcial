from clases.sucursal import Sucursal


class Minimercado(Sucursal):
    def __init__(self, tipo, id, superficie, facturacion, gasto_alquiler):
        super().__init__(tipo, id, superficie, facturacion)
        self.gasto_alquiler = gasto_alquiler
        
    def resultado_comercial(self):
        return super().resultado_comercial() - self.gasto_alquiler
    
    def indice_rentabilidad(self):
        return super().indice_rentabilidad()
    
    def es_rentable(self):
        return self.indice_rentabilidad() > 35
    
    def __str__(self):
        return super().__str__() + " - Tipo de sucursal: Minimercado"