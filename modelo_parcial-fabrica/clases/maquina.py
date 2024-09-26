from clases.mantenimiento_correctivo import MantenimientoCorrectivo
from clases.mantenimietno_preventivo import MantenimientoPreventivo


class Maquina():
    def __init__(self):
        self.mantenimientos = []
        self.cargar_mantenimientos_csv()
    
    def cargar_mantenimientos_csv(self):
        with open("mantenimientos.csv") as file:
            for line in file:
                datos = line.strip().split(",")
                tipo = int(datos[0])
                fecha = datos[1]
                operario = datos[2]
                importe_repuestos = float(datos[3])
                
                if tipo == 1:
                    resultado_mantenimiento = int(datos[4])
                    importe_insumos = int(datos[5])
                    # crear objeto mantenimiento preventivo
                    mantenimiento_preventivo = MantenimientoPreventivo(tipo, fecha, operario, importe_repuestos, resultado_mantenimiento, importe_insumos)
                    self.mantenimientos.append(mantenimiento_preventivo)
                
                if tipo == 2:
                    horas_inactiva = int(datos[4])
                    importe_tecnico = int(datos[5])
                    # crear objeto mantenimiento correctivo
                    mantenimiento_correctivo = MantenimientoCorrectivo(tipo, fecha, operario, importe_repuestos, horas_inactiva, importe_tecnico)
                    self.mantenimientos.append(mantenimiento_correctivo)
                    
            print("Datos cargados con exito")
    
    def suma_gastos(self):
        gastos_total = 0
        for mantenimiento in self.mantenimientos:
            gastos_total += mantenimiento.obtener_costo_mantenimiento()
        return gastos_total
    
    def mantenimientos_caros(self):
        cont_mantenimientos_caros = 0
        for mantenimiento in self.mantenimientos:
            if mantenimiento.es_caro():
                cont_mantenimientos_caros += 1
                
        return cont_mantenimientos_caros
    
    def rotura_mas_larga(self):
        mantenimiento_rotura_mayor = None
        for mantenimiento in self.mantenimientos:
            if mantenimiento.tipo == 2:
                if mantenimiento_rotura_mayor is None or mantenimiento.obtener_horas_inactiva() > mantenimiento_rotura_mayor.obtener_horas_inactiva():
                    mantenimiento_rotura_mayor = mantenimiento
        if mantenimiento_rotura_mayor:
            return f"la rotura mas larga fue en la fecha {mantenimiento_rotura_mayor.fecha}, realizada por el operario {mantenimiento_rotura_mayor.operario} y duro {mantenimiento_rotura_mayor.horas_inactiva} horas"
        else:
            return "No se encontraron mantenimientos correctivos"