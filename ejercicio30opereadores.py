import math

def calcular_circunferencia(radio):
    """
    Calcula la circunferencia de un círculo dado su radio.
    Parámetro:
        radio (float): el radio del círculo
    Retorna:
        float: la circunferencia calculada
    """
    circunferencia = 2 * math.pi * radio
    return circunferencia

def solicitar_radio():
    """
    Solicita al usuario ingresar un radio válido (número positivo).
    Retorna:
        float: el radio ingresado por el usuario
    """
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo (positivo): "))
            if radio <= 0:
                print("El radio debe ser un número positivo. Intente nuevamente.")
            else:
                return radio
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

def mostrar_menu():
    """
    Muestra el menú principal y devuelve la opción seleccionada por el usuario.
    Retorna:
        str: la opción ingresada por el usuario
    """
    print("\n--- Menú ---")
    print("1. Calcular circunferencia")
    print("2. Salir")
    opcion = input("Seleccione una opción (1-2): ")
    return opcion

def confirmar_repetir():
    """
    Pregunta al usuario si desea realizar otra operación.
    Retorna:
        bool: True si desea repetir, False para salir
    """
    while True:
        respuesta = input("¿Desea realizar otra operación? (s/n): ").strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Por favor, ingrese 's' para sí o 'n' para no.")

def main():
    """
    Función principal que controla la ejecución del programa,
    mostrando menú, gestionando la interacción y llamando a funciones auxiliares.
    """
    continuar = True
    while continuar:
        opcion = mostrar_menu()

        if opcion == '1':
            radio = solicitar_radio()
            circunferencia = calcular_circunferencia(radio)
            print(f"La circunferencia del círculo con radio {radio} es: {circunferencia:.2f}")

            continuar = confirmar_repetir()

        elif opcion == '2':
            print("Gracias por usar el programa. ¡Hasta luego!")
            continuar = False

        else:
            print("Opción inválida. Por favor seleccione 1 o 2.")

if __name__ == "__main__":
    main()
