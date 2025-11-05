import math  # Se usa para la raíz cuadrada

def calcular_area_hexagono(lado):
    area = (3 * math.sqrt(3) / 2) * (lado ** 2)
    return area

def mostrar_menu_calculo():
    while True:
        print("--- MENÚ DE CÁLCULO DEL HEXÁGONO ---")
        print("1. Calcular área del hexágono")
        print("2. Regresar al menú principal")
        print("3. Salir del programa")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            realizar_calculo_area()
        elif opcion == "2":
            break  # Regresar al menú principal
        elif opcion == "3":
            print(" Gracias por usar el programa. ¡Hasta pronto!")
            exit()
        else:
            print(" Opción inválida. Intente nuevamente.")

def realizar_calculo_area():
    while True:
        try:
            # ENTRADA
            lado = float(input("\nIngrese la longitud del lado del hexágono: "))
            if lado <= 0:
                print(" El lado debe ser un número positivo.")
                continue

            # PROCESAMIENTO
            area = calcular_area_hexagono(lado)

            # SALIDA
            print(f"El área del hexágono regular con lado {lado} es: {area:.2f} unidades cuadradas.")

        except ValueError:
            print("Error: Debe ingresar un número válido.")
            continue

        # Opción para repetir o regresar
        repetir = input("\n¿Desea calcular otra área? (s/n): ").lower()
        if repetir != "s":
            break

def menu_principal():
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Calcular área de un hexágono regular")
        print("2. Salir del programa")
        opcion = input("Seleccione una opción (1-2): ")

        if opcion == "1":
            mostrar_menu_calculo()
        elif opcion == "2":
            print(" Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print(" Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()
