

def calcular_volumen_piramide(longitud, ancho, altura):
    """
    Calcula el volumen de una pirámide rectangular.
    Fórmula: V = (longitud * ancho * altura) / 3
    """
    volumen = (longitud * ancho * altura) / 3
    return volumen


def mostrar_menu_principal():
    """Muestra el menú principal y devuelve la opción elegida por el usuario."""
    print("===== MENÚ PRINCIPAL =====")
    print("1. Calcular volumen de una pirámide rectangular")
    print("2. Salir del programa")
    opcion = input("Seleccione una opción: ")
    return opcion


def ejecutar_calculo_volumen():
    """
    Controla la interacción con el usuario para calcular
    el volumen de una pirámide rectangular.
    """
    while True:
        print("\n--- Cálculo del volumen de una pirámide ---")
        try:
            longitud = float(input("Ingrese la longitud de la base: "))
            ancho = float(input("Ingrese el ancho de la base: "))
            altura = float(input("Ingrese la altura de la pirámide: "))

            # Procesamiento
            volumen = calcular_volumen_piramide(longitud, ancho, altura)

            # Salida
            print(f"\nEl volumen de la pirámide rectangular es: {volumen:.2f} unidades cúbicas.")
        except ValueError:
            print("Error: por favor ingrese solo valores numéricos válidos.")
            continue

        # Submenú de opciones
        print("\n1. Realizar otro cálculo")
        print("2. Volver al menú principal")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            continue
        elif opcion == "2":
            break
        elif opcion == "3":
            print("Saliendo del programa... ¡Hasta luego!")
            exit()
        else:
            print("Opción no válida. Regresando al menú principal.")
            break


# ---- Función principal ----

def main():
    """Función principal que coordina el flujo general del programa."""
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            ejecutar_calculo_volumen()
        elif opcion == "2":
            print("Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# ---- Punto de entrada ----

if __name__ == "__main__":
    main()
