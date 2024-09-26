from clases.mantenimiento import Mantenimiento


class MantenimientoPreventivo(Mantenimiento):
    def __init__(self, tipo, fecha, operario, importe_repuestos, resultado_mantenimiento, importe_insumos):
        super().__init__(tipo, fecha, operario, importe_repuestos)
        self.resultado_mantenimiento = resultado_mantenimiento
        self.importe_insumos = importe_insumos
        
    def obtener_costo_mantenimiento(self):
        return self.importe_repuestos + self.importe_insumos
    