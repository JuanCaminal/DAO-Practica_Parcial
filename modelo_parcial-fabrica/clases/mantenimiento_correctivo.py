from clases.mantenimiento import Mantenimiento


class MantenimientoCorrectivo(Mantenimiento):
    def __init__(self, tipo, fecha, operario, importe_repuestos, horas_inactiva, importe_tecnico):
        super().__init__(tipo, fecha, operario, importe_repuestos)
        self.horas_inactiva = horas_inactiva
        self.importe_tecnico = importe_tecnico
    
    def obtener_costo_mantenimiento(self):
        return self.importe_repuestos + self.importe_tecnico
    
    def obtener_horas_inactiva(self):
        return self.horas_inactiva