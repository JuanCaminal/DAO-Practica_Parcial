from abc import *


class Vehiculo(ABC):
    def __init__(self, tipo, matricula, marca, modelo, costo_base):
        self.tipo = tipo
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.costo_base = costo_base


    @abstractmethod
    def costo_total_mantenimiento(self):
        pass

    def __str__(self):
        return (f'Tipo: {self.tipo} - Matricula: {self.matricula} - Marca: {self.marca} - Modelo: {self.modelo} - Costo Base: {self.costo_base}.')
