def determinar_mayor(numero1, numero2):
    """
    Determina cuál de los dos números ingresados es mayor
    usando operadores aritméticos.

    Parámetros:
        numero1 (float): primer número ingresado
        numero2 (float): segundo número ingresado

    Retorna:
        float: el número mayor
    """

    diferencia = numero1 - numero2  

    if diferencia > 0:
        mayor = numero1
    elif diferencia < 0:
        mayor = numero2
    else:
        mayor = None  # Son iguales

    return mayor  # Salida

def mostrar_menu():
    """
    Controla el flujo principal del programa.
    Permite realizar cálculos, regresar o salir.
    """
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Determinar el mayor de dos números")
        print("2. Salir")

        opcion = input("Seleccione una opción (1-2): ")

        if opcion == "1":
            menu_mayor_numero()
        elif opcion == "2":
            print("\nGracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("\n⚠️ Opción inválida. Intente nuevamente.")


# Submenú: determina el mayor entre dos números
def menu_mayor_numero():
    """
    Submenú que solicita dos números al usuario,
    determina cuál es el mayor e imprime el resultado.
    """
    while True:
        print("\n--- Determinar el mayor de dos números ---")
        try:
            numero1 = float(input("Ingrese el primer número: "))   # Entrada
            numero2 = float(input("Ingrese el segundo número: "))  # Entrada

            mayor = determinar_mayor(numero1, numero2)  # Procesamiento

            # Salida:
            if mayor is None:
                print(f"Ambos números son iguales: {numero1}")
            else:
                print(f"El número mayor es: {mayor}")

        except ValueError:
            print("⚠️ Entrada no válida. Intente nuevamente.")
            continue

        # Control del flujo:
        opcion = input("¿Desea realizar otro cálculo (S/N)? ").upper()
        if opcion == "N":
            break


# Punto de entrada del programa
if __name__ == "__main__":
    mostrar_menu()
