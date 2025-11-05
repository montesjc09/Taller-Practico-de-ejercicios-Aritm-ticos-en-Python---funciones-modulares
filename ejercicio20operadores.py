def convertir_litros_a_galones(litros):
    """Convierte litros a galones (1 galón = 3.78541 litros). Devuelve el resultado."""
    galones = litros / 3.78541
    return galones


def mostrar_menu():
    """Muestra el menú principal y devuelve la opción elegida."""
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Convertir litros a galones")
    print("2. Salir")
    return input("Seleccione una opción: ")


def realizar_conversion():
    """Realiza conversiones repetidas de litros a galones según el deseo del usuario."""
    while True:
        try:
            litros = float(input("\nIngrese la cantidad en litros: "))
            if litros < 0:
                print("Por favor ingrese un valor positivo.")
                continue
        except ValueError:
            print("Error: Ingrese un número válido.")
            continue

        galones = convertir_litros_a_galones(litros)
        print(f"{litros:.2f} litros equivalen a {galones:.4f} galones.")

        repetir = input("¿Desea realizar otra conversión? (s/n): ").lower()
        if repetir != 's':
            break


def main():
    """Función principal que controla el flujo del programa."""
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            realizar_conversion()
        elif opcion == "2":
            print("¡Gracias por usar el conversor! Hasta luego.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
