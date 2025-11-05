

def convertir_dolares_a_euros(dolares, tasa_cambio):
    """Convierte una cantidad en dólares a euros utilizando una tasa de cambio."""
    euros = dolares * tasa_cambio
    return euros


def pedir_tasa_cambio():
    """Solicita al usuario ingresar la tasa de cambio actual y la devuelve."""
    while True:
        try:
            tasa = float(input("Ingrese la tasa de cambio (1 dólar = ? euros): "))
            if tasa <= 0:
                print("La tasa de cambio debe ser mayor que cero.")
                continue
            return tasa
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido.")


# ----------- FUNCIÓN DE SUBMENÚ -----------
def menu_conversion():
    """Submenú para realizar conversiones de dólares a euros."""
    tasa = pedir_tasa_cambio()

    while True:
        print("\n--- MENÚ DE CONVERSIÓN ---")
        print("1. Convertir dólares a euros")
        print("2. Cambiar tasa de cambio")
        print("3. Regresar al menú anterior")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            try:
                dolares = float(input("Ingrese la cantidad en dólares: "))
                if dolares < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                # PROCESAMIENTO
                euros = convertir_dolares_a_euros(dolares, tasa)
                # SALIDA
                print(f"\n${dolares:.2f} USD equivalen a €{euros:.2f} EUR con una tasa de {tasa:.4f}")
            except ValueError:
                print("Error: Ingrese una cantidad válida.")

            # Preguntar si desea hacer otra conversión
            continuar = input("¿Desea realizar otra conversión? (s/n): ").lower()
            if continuar != "s":
                break

        elif opcion == "2":
            tasa = pedir_tasa_cambio()

        elif opcion == "3":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# ----------- FUNCIÓN PRINCIPAL -----------
def main():
    """Función principal que controla el flujo del programa y los menús."""
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ir al conversor de dólares a euros")
        print("2. Salir del programa")

        opcion = input("Seleccione una opción (1-2): ")

        if opcion == "1":
            menu_conversion()
        elif opcion == "2":
            print("Gracias por usar el conversor. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


# ----------- EJECUCIÓN DEL PROGRAMA -----------
if __name__ == "__main__":
    main()
