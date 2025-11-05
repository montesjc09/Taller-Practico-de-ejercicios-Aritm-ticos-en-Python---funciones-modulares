def calcular_cociente(numero1, numero2):
    """
    Calcula el cociente entero de una división entre dos números.
    Parámetros:
        numero1 (int): Dividendo
        numero2 (int): Divisor
    Retorna:
        int: Cociente entero de la división
    """
    # Validar que el divisor no sea cero
    if numero2 == 0:
        print("Error: No se puede dividir entre cero.")
        return None
    else:
        cociente = numero1 // numero2  # División entera
        return cociente


# Función que muestra el submenú de cálculo
def mostrar_submenu():
    """
    Muestra un menú para calcular el cociente de divisiones enteras.
    Permite realizar varios cálculos o regresar al menú principal.
    """
    while True:
        print("\n--- MENÚ DE CÁLCULOS ---")
        print("1. Calcular cociente de una división entera")
        print("2. Regresar al menú principal")

        opcion = input("Seleccione una opción (1-2): ")

        if opcion == "1":
            # Entrada de datos
            numero1 = int(input("Ingrese el primer número entero (dividendo): "))
            numero2 = int(input("Ingrese el segundo número entero (divisor): "))

            # Procesamiento
            resultado = calcular_cociente(numero1, numero2)

            # Salida
            if resultado is not None:
                print(f"El cociente entero de {numero1} ÷ {numero2} es: {resultado}")

        elif opcion == "2":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

        # Preguntar si desea repetir
        repetir = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if repetir != "s":
            print("Regresando al menú de cálculos...")
            break


# Función principal
def main():
    """
    Controla el flujo principal del programa.
    Presenta el menú principal y gestiona las opciones del usuario.
    """
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ir al menú de cálculos")
        print("2. Salir del programa")

        opcion = input("Seleccione una opción (1-2): ")

        if opcion == "1":
            mostrar_submenu()
        elif opcion == "2":
            print("Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# --- Ejecución del programa ---
if __name__ == "__main__":
    main()
