def solicitar_numero(mensaje):
    """
    Solicita al usuario un número válido (float).
    Parámetros:
        mensaje (str): Texto que se muestra para pedir el dato.
    Retorna:
        numero (float): Número ingresado por el usuario.
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def calcular_suma(num1, num2):
    """
    Calcula la suma de dos números.
    Parámetros:
        num1 (float): Primer número.
        num2 (float): Segundo número.
    Retorna:
        suma (float): Resultado de la suma.
    """
    return num1 + num2

def mostrar_menu_post_calculo():
    """
    Muestra el menú después de mostrar el resultado y pide opción.
    Retorna:
        opcion (str): Opción elegida por el usuario.
    """
    print("\n¿Qué desea hacer ahora?")
    print("1. Realizar otra suma")
    print("2. Regresar al inicio")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")
    return opcion

def menu_principal():
    """
    Controla el flujo del programa mostrando menú principal y
    gestionando la interacción con el usuario.
    """
    while True:
        print("--- SUMA DE DOS NÚMEROS ---")

        # Solicitar números
        num1 = solicitar_numero("Ingrese el primer número: ")
        num2 = solicitar_numero("Ingrese el segundo número: ")

        # Calcular suma
        resultado = calcular_suma(num1, num2)

        # Mostrar resultado
        print(f"La suma de {num1} + {num2} es: {resultado}")

        # Menú post cálculo
        while True:
            opcion = mostrar_menu_post_calculo()
            if opcion == '1':
                # Repetir cálculo
                break  # rompe este while y repite el externo
            elif opcion == '2':
                # Regresar al inicio (menú principal)
                break  # igual que arriba, en este caso se repite el ciclo externo
            elif opcion == '3':
                print("Gracias por usar el programa. ¡Adiós!")
                return  # sale del programa
            else:
                print("Opción inválida. Intente de nuevo.")

def main():
    """
    Función principal para iniciar el programa.
    """
    print("Bienvenido al programa de suma de dos números")
    menu_principal()

if __name__ == "__main__":
    main()
