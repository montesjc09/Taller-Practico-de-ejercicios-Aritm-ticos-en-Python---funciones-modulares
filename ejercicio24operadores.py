def solicitar_numero(mensaje):
    """
    Solicita un número al usuario, validando que la entrada sea numérica.
    Parámetros:
        mensaje (str): Mensaje para pedir el número.
    Retorna:
        float: Número ingresado por el usuario.
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

def calcular_cuadrado(numero):
    """
    Calcula el cuadrado de un número usando el operador de multiplicación.
    Parámetros:
        numero (float): Número a elevar al cuadrado.
    Retorna:
        float: Resultado del cuadrado del número.
    """
    return numero * numero

def repetir_o_salir():
    """
    Pregunta al usuario si desea repetir la operación o salir.
    Retorna:
        str: 'repetir' para hacer otro cálculo,
             'menu' para regresar al menú,
             'salir' para terminar el programa.
    """
    while True:
        print("\nSeleccione una opción:")
        print("1. Realizar otro cálculo")
        print("2. Regresar al menú principal")
        print("3. Salir")
        opcion = input("Ingrese 1, 2 o 3: ")

        if opcion == "1":
            return 'repetir'
        elif opcion == "2":
            return 'menu'
        elif opcion == "3":
            return 'salir'
        else:
            print("Opción inválida, intente nuevamente.")

def menu_cuadrado():
    """
    Menú para calcular el cuadrado de un número.
    Controla la interacción para repetir cálculos o regresar al menú principal.
    """
    while True:
        numero = solicitar_numero("\nIngrese un número para calcular su cuadrado: ")
        resultado = calcular_cuadrado(numero)
        print(f"El cuadrado de {numero} es: {resultado}")

        accion = repetir_o_salir()
        if accion == 'repetir':
            continue  # Repite el cálculo
        elif accion == 'menu':
            break     # Regresa al menú principal
        elif accion == 'salir':
            print("Gracias por usar el programa. ¡Hasta luego!")
            exit()    # Sale del programa

def main():
    """
    Función principal que controla el flujo general del programa.
    Presenta el menú principal y permite acceder al cálculo o salir.
    """
    while True:
        print("\n=== Menú Principal ===")
        print("1. Calcular el cuadrado de un número")
        print("2. Salir")
        opcion = input("Seleccione una opción (1-2): ")

        if opcion == "1":
            menu_cuadrado()
        elif opcion == "2":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()
