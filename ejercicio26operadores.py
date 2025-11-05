def mostrar_menu_principal():
    """
    Muestra el menú principal y solicita al usuario seleccionar una opción.
    Retorna la opción seleccionada como entero.
    """
    print("=== Menú Principal ===")
    print("1. Calcular residuo de división")
    print("2. Salir")

    while True:
        try:
            opcion = int(input("Seleccione una opción (1-2): "))
            if opcion in [1, 2]:
                return opcion
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Ingrese un número.")


def solicitar_numeros():
    """
    Solicita dos números enteros al usuario.
    Retorna una tupla con dos valores enteros.
    """
    while True:
        try:
            num1 = int(input("Ingrese el dividendo (número entero): "))
            num2 = int(input("Ingrese el divisor (número entero, distinto de cero): "))
            if num2 == 0:
                print("El divisor no puede ser cero. Intente de nuevo.")
                continue
            return num1, num2
        except ValueError:
            print("Entrada no válida. Por favor, ingrese números enteros válidos.")


def calcular_residuo(dividendo, divisor):
    """
    Recibe dos números enteros y devuelve el residuo de la división (dividendo % divisor).
    """
    return dividendo % divisor


def menu_residuo():
    """
    Controla el flujo para la operación de cálculo de residuo.
    Permite realizar múltiples cálculos, regresar al menú principal o salir.
    """
    while True:
        print("--- Cálculo de residuo ---")
        dividendo, divisor = solicitar_numeros()
        resultado = calcular_residuo(dividendo, divisor)
        print(f"El residuo de la división de {dividendo} entre {divisor} es: {resultado}")

        print("\n¿Qué desea hacer ahora?")
        print("1. Realizar otro cálculo")
        print("2. Regresar al menú principal")
        print("3. Salir")

        while True:
            try:
                opcion = int(input("Seleccione una opción (1-3): "))
                if opcion == 1:
                    # Repetir cálculo
                    break
                elif opcion == 2:
                    # Regresar al menú principal
                    return
                elif opcion == 3:
                    # Salir del programa
                    print("Gracias por usar el programa. ¡Hasta luego!")
                    exit()
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada no válida. Ingrese un número.")


def main():
    """
    Función principal que controla la ejecución del programa.
    """
    print("Bienvenido al programa para calcular el residuo de una división.")
    while True:
        opcion = mostrar_menu_principal()

        if opcion == 1:
            menu_residuo()
        elif opcion == 2:
            print("Gracias por usar el programa. ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
