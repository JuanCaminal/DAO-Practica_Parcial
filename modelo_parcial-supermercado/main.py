from clases.empresa import Empresa


def main():
    empresa = Empresa()
    print(f"La suma de ganancias es: {empresa.suma_ganancia()}")
    print(f"La cantidad de locales no rentables son: {empresa.cantidad_locales_no_rentables()}")
    print(f"{empresa.local_mas_rentable()}")
    
if __name__ == "__main__":
    main()