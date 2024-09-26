from classes.empresa import Empresa


def main():
    empresa = Empresa()
    print(f'Vehiculo con mayor costo de mantenimiento: {empresa.obtener_vehiculo_mayor_mantenimiento()}')
    print(f'Cantidad de camionetas con maas de 1000 kg de capacidad de carga: {empresa.contar_camionetas_mas_capacidad()}')
    print(f'Cantidad de motos de alta cilindrada: {empresa.contar_motos_alta_cilindrada()}')
if __name__ == "__main__":
    main()