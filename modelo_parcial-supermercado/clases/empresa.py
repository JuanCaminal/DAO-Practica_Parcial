from clases.hipermercado import Hipermercado
from clases.minimercado import Minimercado
from clases.supermercado import Supermercado


class Empresa():
    def __init__(self) -> None:
        self.sucursales = []
        self.cargar_sucursales_csv()
        
    def cargar_sucursales_csv(self):
        with open("sucursales.csv") as file:
            for line in file:
                datos = line.strip().split(",")
                tipo = int(datos[0])
                id = int(datos[1])
                superficie = int(datos[2])
                facturacion = float(datos[3])
                
                if tipo == 1:   # Hipermercados
                    importe_alquileres = int(datos[4])
                    hipermercado = Hipermercado(tipo, id, superficie, facturacion, importe_alquileres)
                    self.sucursales.append(hipermercado)
                elif tipo == 2: # Supermercados
                    tipo_super = int(datos[4])
                    supermercado = Supermercado(tipo, id, superficie, facturacion, tipo_super)
                    self.sucursales.append(supermercado)
                elif tipo == 3: # Minimercados
                    gasto_alquiler = int(datos[4])
                    minimercado = Minimercado(tipo, id, superficie, facturacion, gasto_alquiler)
                    self.sucursales.append(minimercado)
                    
            print("Sucursales cargadas con exito")
    
    def suma_ganancia(self):
        suma_ganancias = 0
        for sucursal in self.sucursales:
            suma_ganancias += sucursal.resultado_comercial()
        return suma_ganancias
    
    def cantidad_locales_no_rentables(self):
        contador = 0
        for sucursal in self.sucursales:
            if not sucursal.es_rentable():
                contador += 1
        return contador
    
    def local_mas_rentable(self):
        local_mas_rentable = self.sucursales[0]
        for sucursal in self.sucursales:
            if sucursal.indice_rentabilidad() > local_mas_rentable.indice_rentabilidad():
                local_mas_rentable = sucursal
        return str(local_mas_rentable)