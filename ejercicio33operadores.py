def solicitar_distancia():
    """
    Solicita al usuario una distancia en kilómetros.
    Entradas: ninguna (solicita dato al usuario)
    Procesamiento: convierte el valor a tipo float
    Salida: retorna la distancia en kilómetros
    """
    km = float(input("Ingrese la distancia en kilómetros: "))
    return km


def convertir_a_millas(kilometros):
    """
    Convierte kilómetros a millas.
    Entradas: kilometros (float)
    Procesamiento: aplica la fórmula millas = km * 0.621371
    Salida: retorna el valor en millas
    """
    millas = kilometros * 0.621371
    return millas


def mostrar_resultado(km, millas):
    """
    Muestra el resultado de la conversión.
    Entradas: km (float), millas (float)
    Procesamiento: genera un mensaje con formato
    Salida: imprime el resultado
    """
    print(f"{km:.2f} kilómetros equivalen a {millas:.2f} millas.")


def menu_conversion():
    """
    Permite realizar la conversión de kilómetros a millas
    y controla si el usuario desea repetir, regresar o salir.
    """
    while True:
        print("\n--- CONVERSIÓN DE KILÓMETROS A MILLAS ---")
        km = solicitar_distancia()
        millas = convertir_a_millas(km)
        mostrar_resultado(km, millas)

        print("¿Qué desea hacer ahora?")
        print("1. Realizar otra conversión")
        print("2. Regresar al menú principal")
        print("3. Salir del programa")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            continue  # Repite la conversión
        elif opcion == "2":
            break      # Regresa al menú principal
        elif opcion == "3":
            print("\nGracias por usar el programa. ¡Hasta pronto!\n")
            exit()
        else:
            print("\nOpción inválida. Intente nuevamente.\n")


def menu_principal():
    """
    Presenta el menú principal del programa y permite al usuario
    elegir entre realizar una conversión o salir.
    """
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Convertir kilómetros a millas")
        print("2. Salir")
        print("===================================")

        opcion = input("Seleccione una opción (1-2): ")

        if opcion == "1":
            menu_conversion()
        elif opcion == "2":
            print("\nGracias por usar el programa. ¡Hasta pronto!\n")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.\n")


def main():
    """
    Función principal del programa.
    Controla la ejecución general.
    """
    menu_principal()


# Punto de entrada del programa
if __name__ == "__main__":
    main()
