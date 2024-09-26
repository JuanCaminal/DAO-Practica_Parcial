from clases.auto import Auto
from clases.camioneta import Camioneta
from clases.moto import Moto


class Empresa():
    def __init__(self):
        self.vehiculos = []
        self.cargar_datos_csv()
        
    def cargar_datos_csv(self):
        with open("vehiculos.csv") as file:
            for line in file:
                datos = line.strip().split(",")
                tipo = int(datos[0])
                marca = datos[1]
                matricula = datos[2]
                modelo = int(datos[3])
                costo_base = float(datos[4])
                
                match tipo:
                    case 1:
                        kilometraje = int(datos[5])
                        
                        auto = Auto(tipo, matricula, marca, modelo, costo_base, kilometraje) 
                        self.vehiculos.append(auto)
                    case 2:
                        capacidad_carga = int(datos[5])
                        
                        camioneta = Camioneta(tipo, matricula, marca, modelo, costo_base, capacidad_carga)
                        self.vehiculos.append(camioneta)
                    case 3:
                        cc = int(datos[5])
                        
                        moto = Moto(tipo, matricula, marca, modelo, costo_base, cc)
                        self.vehiculos.append(moto)
            print("Datos cargados con exito")
    
    def calcular_costos_mantenimiento(self):
        costos = 0
        for vehiculo in self.vehiculos:
            costos += vehiculo.costo_base
        return costos
    
    def calcular_costos_mantenimiento_con_incrementos(self):
        costos = 0
        for vehiculos in self.vehiculos:
            costos += vehiculos.costo_mantenimiento()
        return costos
    