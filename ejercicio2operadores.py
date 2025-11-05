import math

def mostrar_menu_principal():
    """
    Muestra el menú principal para calcular el volumen de una esfera o salir del programa.
    """
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Calcular el volumen de una esfera")
    print("2. Salir")

    while True:
        opcion = input("Seleccione una opción (1-2): ")
        if opcion in ['1', '2']:
            return opcion
        else:
            print("Opción inválida. Por favor, elija 1 o 2.")


def solicitar_radio():
    """
    Solicita al usuario que ingrese el radio de la esfera. Retorna el valor como flotante.
    """
    while True:
        try:
            radio = float(input("Ingrese el radio de la esfera: "))
            if radio > 0:
                return radio
            else:
                print("El radio debe ser un número positivo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido para el radio.")


def calcular_volumen_esfera(radio):
    """
    Calcula el volumen de una esfera dado su radio.
    Parámetros:
    radio (float): Radio de la esfera.
    Retorna:
      float: Volumen calculado.
    """
    volumen = (4/3) * math.pi * (radio ** 3)
    return volumen


def preguntar_repetir():
    """
    Pregunta al usuario si desea realizar otro cálculo, volver al menú principal o salir.
    Retorna la elección del usuario.
    """
    print("\n¿Qué desea hacer ahora?")
    print("1. Calcular otro volumen")
    print("2. Volver al menú principal")
    print("3. Salir")

    while True:
        eleccion = input("Seleccione una opción (1-3): ")
        if eleccion in ['1', '2', '3']:
            return eleccion
        else:
            print("Opción inválida. Intente de nuevo.")


def ejecutar_calculo_volumen():
    """
    Ejecuta el proceso de solicitud del radio, cálculo del volumen
    y muestra el resultado. Controla si repetir, volver o salir.
    """
    while True:
        radio = solicitar_radio()
        volumen = calcular_volumen_esfera(radio)

        print(f"\nEl volumen de la esfera con radio {radio} es: {volumen:.2f} unidades cúbicas.")

        siguiente_paso = preguntar_repetir()

        if siguiente_paso == '1':
            continue  # Repetir cálculo
        elif siguiente_paso == '2':
            break  # Volver al menú principal
        else:
            print("Gracias por usar el programa.")
            exit()


def main():
    """
    Función principal que muestra el menú y gestiona la navegación del usuario.
    """
    print("=== BIENVENIDO AL CALCULADOR DE VOLUMEN DE UNA ESFERA ===")
    while True:
        opcion = mostrar_menu_principal()

        if opcion == '1':
            ejecutar_calculo_volumen()
        elif opcion == '2':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break


# Punto de entrada del programa
if __name__ == "__main__":
    main()
