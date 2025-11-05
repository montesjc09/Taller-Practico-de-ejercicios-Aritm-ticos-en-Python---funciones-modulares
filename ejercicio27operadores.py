def mostrar_menu():
    """
    Muestra el menú principal para que el usuario elija una acción.
    Devuelve la opción elegida como string.
    """
    print("\n=== Menú ===")
    print("1. Calcular raíz cuadrada de un número")
    print("2. Salir")
    opcion = input("Seleccione una opción (1-2): ")
    return opcion


def pedir_numero_positivo():
    """
    Solicita al usuario un número positivo para calcular su raíz cuadrada.
    Verifica que el número sea válido.
    Devuelve el número como float.
    """
    while True:
        try:
            num = float(input("Ingrese un número positivo: "))
            if num < 0:
                print("Error: El número no puede ser negativo.")
            else:
                return num
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido.")


def calcular_raiz_cuadrada(numero, tolerancia=1e-10, max_iter=1000):
    """
    Calcula la raíz cuadrada de un número usando el método de Newton-Raphson.
    Parámetros:
        - numero: número del que se desea calcular la raíz cuadrada.
        - tolerancia: diferencia máxima permitida para la aproximación.
        - max_iter: número máximo de iteraciones para evitar loops infinitos.
    Devuelve la raíz cuadrada aproximada.
    """
    if numero == 0:
        return 0.0

    # Valor inicial aproximado (puede ser el mismo número o la mitad)
    aproximacion = numero / 2.0

    for _ in range(max_iter):
        # Nueva aproximación usando Newton-Raphson
        siguiente = (aproximacion + numero / aproximacion) / 2.0

        # Verificamos si la diferencia es menor que la tolerancia
        if abs(siguiente - aproximacion) < tolerancia:
            return siguiente

        aproximacion = siguiente

    # Si no converge, devuelve la última aproximación
    return aproximacion


def menu_calcular_raiz():
    """
    Controla el flujo para calcular raíz cuadrada, mostrar resultado y
    permitir repetir o salir.
    """
    while True:
        numero = pedir_numero_positivo()  # Entrada

        raiz = calcular_raiz_cuadrada(numero)  # Procesamiento

        # Salida
        print(f"La raíz cuadrada aproximada de {numero} es: {raiz}")

        # Menú después del cálculo
        print("\n¿Qué desea hacer ahora?")
        print("1. Calcular otra raíz cuadrada")
        print("2. Volver al menú principal")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            continue
        elif opcion == '2':
            break
        elif opcion == '3':
            print("Gracias por usar el programa. ¡Hasta luego!")
            exit()
        else:
            print("Opción inválida. Regresando al menú principal.")
            break


def main():
    """
    Función principal que controla el menú general y la ejecución del programa.
    """
    print("Bienvenido al programa de cálculo de raíz cuadrada")

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            menu_calcular_raiz()
        elif opcion == '2':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")


if __name__ == "__main__":
    main()
