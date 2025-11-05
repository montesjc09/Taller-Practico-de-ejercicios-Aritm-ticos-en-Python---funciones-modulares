
def convertir_pulgadas_a_centimetros(pulgadas):
    centimetros = pulgadas * 2.54  # 1 pulgada = 2.54 cm
    return centimetros


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Convertir pulgadas a centímetros")
    print("2. Salir del programa")
    opcion = input("Seleccione una opción: ")
    return opcion



def realizar_conversion():
    while True:
        print("\n--- CONVERSIÓN DE PULGADAS A CENTÍMETROS ---")
        try:
            pulgadas = float(input("Ingrese la longitud en pulgadas: "))

            # Procesamiento
            centimetros = convertir_pulgadas_a_centimetros(pulgadas)

            # Salida
            print(f"\n{pulgadas} pulgadas equivalen a {centimetros:.2f} centímetros.")

        except ValueError:
            print("Error: Ingrese solo valores numéricos.")
            continue

        # Submenú de opciones después de la conversión
        print("\n¿Qué desea hacer ahora?")
        print("1. Realizar otra conversión")
        print("2. Regresar al menú principal")
        print("3. Salir del programa")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            continue
        elif eleccion == "2":
            break
        elif eleccion == "3":
            print("Gracias por usar el programa. ¡Hasta luego!")
            exit()
        else:
            print("Opción no válida. Regresando al menú principal.")
            break


def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            realizar_conversion()
        elif opcion == "2":
            print("Programa finalizado. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# ------------------------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
