from clases.sucursal import Sucursal

class Supermercado(Sucursal):
    def __init__(self, tipo, id, superficie, facturacion, tipo_super):
        super().__init__(tipo, id, superficie, facturacion)
        self.tipo_super = tipo_super
        
    def indice_rentabilidad(self):
        return super().indice_rentabilidad()
    
    def es_rentable(self):
        if self.tipo_super == 1:
            return self.indice_rentabilidad() > 45
        return self.indice_rentabilidad() > 40
    
    def __str__(self):
        return super().__str__() + " - Tipo de sucursal: Supermercado"