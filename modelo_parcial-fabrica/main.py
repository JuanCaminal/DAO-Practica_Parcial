from clases.maquina import Maquina


def main():
    mantenimiento = Maquina()
    
    print(f"Suma de gastos: {mantenimiento.suma_gastos()}")
    print(f"Cantidad de mantenimientos caros: {mantenimiento.mantenimientos_caros()}")
    print(f"Rotura mas larga: {mantenimiento.rotura_mas_larga()}")

if __name__ == "__main__":
    main()