def calcular_descuento(precio):
    """
    Calcula el 10% de descuento sobre el precio del artículo.
    Entrada: precio (float)
    Proceso: descuento = precio * 0.10
             precio_final = precio - descuento
    Salida: tupla (descuento, precio_final)
    """
    descuento = precio * 0.10
    precio_final = precio - descuento
    return descuento, precio_final


def mostrar_menu_principal():
    """
    Muestra el menú principal y solicita la opción del usuario.
    """
    print("=== MENÚ PRINCIPAL ===")
    print("1. Calcular descuento del 10%")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def menu_calcular_descuento():
    """
    Submenú que permite calcular el descuento del 10% sobre el precio ingresado.
    Permite repetir cálculos, regresar o salir.
    """
    while True:
        try:
            precio = float(input("Ingrese el precio del artículo: "))
            descuento, precio_final = calcular_descuento(precio)

            print("--- RESULTADO ---")
            print(f"Precio original: ${precio:.2f}")
            print(f"Descuento (10%): ${descuento:.2f}")
            print(f"Precio final: ${precio_final:.2f}")

            print("\n¿Desea realizar otro cálculo?")
            print("1. Sí")
            print("2. Regresar al menú anterior")
            print("3. Salir del programa")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                continue  # Repite el cálculo
            elif opcion == "2":
                break     # Regresa al menú principal
            elif opcion == "3":
                exit()    # Termina el programa
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

def main():
    """
    Función principal que controla el flujo del programa.
    """
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            menu_calcular_descuento()
        elif opcion == "2":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
