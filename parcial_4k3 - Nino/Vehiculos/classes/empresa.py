
from classes.camioneta import *
from classes.auto import Auto
from classes.moto import *

class Empresa():
    def __init__(self):
        self.vehiculos = []
        self.cargar_datos_csv()

    def cargar_datos_csv(self):
        with open('vehiculos.csv') as file:
            for line in file:
                datos = line.strip().split(',')
                tipo = int(datos[0])
                marca = datos[1]
                modelo = int(datos[3])
                matricula = datos[2]
                costo_base = float(datos[4])

                if tipo == 1:
                    # auto
                    kilometraje = int(datos[5])
                    self.vehiculos.append(
                        Auto(tipo, matricula, marca, modelo, costo_base, kilometraje)
                    )
                elif tipo == 2:
                    # camioneta
                    capacidad_carga = int(datos[5])
                    self.vehiculos.append(
                        Camioneta(tipo, matricula, marca, modelo, costo_base, capacidad_carga)
                    )
                elif tipo == 3:
                    # moto
                    cilindrada = int(datos[5])
                    self.vehiculos.append(
                        Moto(tipo, matricula, marca, modelo, costo_base, cilindrada)
                    )
        print("Datos cargados con exito!")

    def calcular_costos_mantenimiento(self):
        suma = 0
        for vehiculo in self.vehiculos:
            suma += vehiculo.costo_base
        return suma

    def obtener_vehiculo_mayor_mantenimiento(self):
        vehiculo_mayor_mantenimiento = self.vehiculos[0]
        for vehiculo in self.vehiculos:
            if vehiculo.costo_total_mantenimiento() > vehiculo_mayor_mantenimiento.costo_total_mantenimiento():
                vehiculo_mayor_mantenimiento = vehiculo
        return vehiculo_mayor_mantenimiento

    def contar_camionetas_mas_capacidad(self):
        cont = 0
        for vehiculo in self.vehiculos:
            if vehiculo.tipo == 2 and vehiculo.capacidad_carga > 1000:
                cont += 1
        return cont

    def contar_motos_alta_cilindrada(self):
        cont = 0
        for vehiculo in self.vehiculos:
            if vehiculo.tipo == 3 and vehiculo.cilindrada > 500:
                cont += 1
        return cont
