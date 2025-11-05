import math

def mostrar_menu_principal():
    """
    Muestra el menú principal del programa.
    """
    print("--- MENÚ PRINCIPAL ---")
    print("1. Calcular el volumen de un cilindro")
    print("2. Salir")


def solicitar_valor_positivo(nombre_variable):
    """
    Solicita al usuario un número positivo (float) para el radio o altura.

    Parámetros:
        nombre_variable (str): nombre del valor solicitado, para mostrar en pantalla.

    Retorna:
        float: valor positivo ingresado por el usuario.
    """
    while True:
        try:
            valor = float(input(f"Ingrese el {nombre_variable} (positivo): "))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")


def calcular_volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro usando la fórmula V = π * r^2 * h

    Parámetros:
        radio (float): radio de la base del cilindro
        altura (float): altura del cilindro

    Retorna:
        float: volumen calculado
    """
    volumen = math.pi * radio ** 2 * altura
    return volumen


def mostrar_resultado_volumen(radio, altura, volumen):
    """
    Muestra el resultado del cálculo de volumen de forma clara.

    Parámetros:
        radio (float): radio del cilindro
        altura (float): altura del cilindro
        volumen (float): volumen calculado
    """
    print(f"\n--- RESULTADO ---")
    print(f"Radio ingresado: {radio}")
    print(f"Altura ingresada: {altura}")
    print(f"Volumen del cilindro: {volumen:.2f} unidades cúbicas")


def ejecutar_calculo_volumen():
    """
    Ejecuta el flujo de cálculo del volumen: solicita datos, calcula y muestra.
    """
    radio = solicitar_valor_positivo("radio de la base")
    altura = solicitar_valor_positivo("altura")

    volumen = calcular_volumen_cilindro(radio, altura)
    mostrar_resultado_volumen(radio, altura, volumen)


def ejecutar_programa():
    """
    Función principal que controla el menú y flujo general del programa.
    """
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            while True:
                ejecutar_calculo_volumen()
                repetir = input("\n¿Desea calcular otro volumen? (s/n): ").lower()
                if repetir != 's':
                    break

        elif opcion == '2':
            print("Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el programa principal
ejecutar_programa()





