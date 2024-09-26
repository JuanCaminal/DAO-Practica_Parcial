from clases.sucursal import Sucursal


class Hipermercado(Sucursal):
    def __init__(self, tipo, id, superficie, facturacion, importe_alquileres):
        super().__init__(tipo, id, superficie, facturacion)
        self.importe_alquileres = importe_alquileres
        
    def resultado_comercial(self):
        return super().resultado_comercial() + self.importe_alquileres
    
    def indice_rentabilidad(self):
        return super().indice_rentabilidad()
    
    def es_rentable(self):
        return self.indice_rentabilidad() > 50
    
    def __str__(self):
        return super().__str__() + " - Tipo de sucursal: Hipermercado"