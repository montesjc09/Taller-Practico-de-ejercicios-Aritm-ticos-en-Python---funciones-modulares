import math

def mostrar_menu_principal():
    """
    Muestra el menú principal con opciones al usuario.
    """
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Calcular el área de un círculo")
    print("2. Salir")
    
    opcion = input("Seleccione una opción (1-2): ")
    return opcion


def solicitar_radio():
    """
    Solicita el radio al usuario, validando que sea un número positivo.
    """
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        if radio < 0:
            print("Error: El radio no puede ser negativo.")
            return solicitar_radio()
        return radio
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        return solicitar_radio()


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    Parámetros:
 radio (float): radio del círculo.
    Retorna:
        float: área del círculo.
    """
    area = math.pi * radio ** 2
    return area


def realizar_calculo_area():
    """
    Coordina la solicitud del radio, el cálculo y la presentación del resultado.
    """
    radio = solicitar_radio()
    area = calcular_area_circulo(radio)
    print(f"\nEl área del círculo con radio {radio} es: {area:.2f}")


def preguntar_repetir():
    """
    Pregunta al usuario si desea repetir, volver al menú o salir.
    """
    print("\n¿Qué desea hacer ahora?")
    print("1. Calcular otro área")
    print("2. Volver al menú principal")
    print("3. Salir")
    opcion = input("Ingrese su opción: ")
    return opcion


def main():
    """
    Función principal que controla el flujo del programa.
    """
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == '1':
            while True:
                realizar_calculo_area()
                siguiente = preguntar_repetir()
                
                if siguiente == '1':
                    continue
                elif siguiente == '2':
                    break
                elif siguiente == '3':
                    print("Gracias por usar el programa. ¡Hasta luego!")
                    return
                else:
                    print("Opción inválida. Regresando al menú principal.")
                    break
        
        elif opcion == '2':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    main()

