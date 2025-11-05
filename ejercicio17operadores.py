def convertir_libras_a_kilogramos(libras):
    kilogramos = libras * 0.453592  # 1 libra = 0.453592 kg
    return kilogramos

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Convertir libras a kilogramos")
    print("2. Salir del programa")
    opcion = input("Seleccione una opción (1-2): ")
    return opcion

def realizar_conversion():
    # Entrada
    libras = float(input("Ingrese el peso en libras: "))

    # Procesamiento
    kilogramos = convertir_libras_a_kilogramos(libras)

    # Salida
    print(f"{libras} libras equivalen a {kilogramos:.3f} kilogramos.")

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            realizar_conversion()

            # Preguntar si desea realizar otra conversión
            continuar = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
            if continuar != "s":
                print("Volviendo al menú principal...")

        elif opcion == "2":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


# ---------------------------------------------------------
# Punto de entrada del programa
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
