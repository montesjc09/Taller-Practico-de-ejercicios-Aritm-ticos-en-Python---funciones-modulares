def convertir_kilometros_a_millas(kilometros):
    """
    Convierte una distancia en kilómetros a millas.
    Parámetros:
        kilometros (float): distancia en kilómetros
    Retorna:
        float: distancia equivalente en millas
    """
    millas = kilometros * 0.621371  # 1 km = 0.621371 millas
    return millas


# Función que maneja el submenú de conversión
def mostrar_menu_conversion():
    """
    Muestra el menú de conversión y permite al usuario realizar
    varias conversiones o regresar al menú principal.
    """
    while True:
        print("\n--- MENÚ DE CONVERSIÓN ---")
        print("1. Convertir kilómetros a millas")
        print("2. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            kilometros = float(input("\nIngrese la distancia en kilómetros: "))

            resultado = convertir_kilometros_a_millas(kilometros)

            print(f"\n{kilometros} kilómetros equivalen a {resultado:.3f} millas.")
            
            while True:
                print("\n¿Desea realizar otra conversión?")
                print("1. Sí")
                print("2. No (regresar al menú de conversión)")
                decision = input("Seleccione una opción: ")

                if decision == "1":
                    break  # Repite la conversión
                elif decision == "2":
                    return  # Regresa al menú principal
                else:
                    print("Opción inválida. Intente de nuevo.")

        elif opcion == "2":
            # Regresar al menú principal
            print("\nRegresando al menú principal...")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


# Función principal del programa
def main():
    """
    Función principal que controla el flujo general del programa.
    Muestra el menú principal y permite acceder a las conversiones o salir.
    """
    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Realizar conversión de kilómetros a millas")
        print("2. Salir del programa")
        print("==================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_menu_conversion()
        elif opcion == "2":
            print("\nSaliendo del programa... ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
