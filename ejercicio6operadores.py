import math

def mostrar_menu_principal():
    """Muestra el menú principal del programa."""
    print("==== MENÚ PRINCIPAL ====")
    print("1. Calcular volumen de un cono")
    print("2. Salir")


def solicitar_valor_positivo(mensaje):
    """
    Solicita al usuario un número positivo.
    :param mensaje: Texto mostrado al usuario.
    :return: Número float validado como positivo.
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Por favor, ingrese un valor positivo.")
        except ValueError:
            print(" Entrada inválida. Intente nuevamente con un número válido.")


def calcular_volumen_cono(radio, altura):
    """
    Calcula el volumen de un cono usando la fórmula: V = (1/3) * π * r^2 * h
    :param radio: Radio de la base del cono.
    :param altura: Altura del cono.
    :return: Volumen calculado (float).
    """
    volumen = (1/3) * math.pi * radio**2 * altura
    return volumen


def ejecutar_calculo_cono():
    """
    Ejecuta la interacción para calcular el volumen del cono.
    Permite al usuario repetir el cálculo o volver al menú anterior.
    """
    while True:
        print("--- Cálculo del Volumen de un Cono ---")
        radio = solicitar_valor_positivo("Ingrese el radio de la base (cm): ")
        altura = solicitar_valor_positivo("Ingrese la altura (cm): ")

        # Procesamiento
        volumen = calcular_volumen_cono(radio, altura)

        # Salida
        print(f" El volumen del cono es: {volumen:.2f} cm³")

        # Repetir o volver
        print("\n¿Desea realizar otro cálculo?")
        print("1. Sí, calcular otro volumen")
        print("2. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion != '1':
            break


def ejecutar_programa():
    """Función principal del programa: controla el flujo principal."""
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-2): ")

        if opcion == '1':
            ejecutar_calculo_cono()
        elif opcion == '2':
            print(" Gracias por usar el programa. ¡Hasta la próxima!")
            break
        else:
            print(" Opción inválida. Intente nuevamente.")


# --- Punto de entrada del programa ---
if __name__ == "__main__":
    ejecutar_programa()
