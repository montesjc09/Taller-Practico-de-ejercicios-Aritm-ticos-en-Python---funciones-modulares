def pedir_numero(mensaje):
    """
    Solicita al usuario un número (puede ser positivo o negativo) y lo devuelve.
    Parámetro:
        mensaje (str): texto para mostrar al usuario.
    Retorna:
        float: número ingresado por el usuario.
    """
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

def calcular_resta(num1, num2):
    """
    Calcula la resta de num1 menos num2.
    Parámetros:
        num1 (float): minuendo.
        num2 (float): sustraendo.
    Retorna:
        float: resultado de la resta.
    """
    resultado = num1 - num2
    return resultado

def mostrar_menu():
    """
    Muestra el menú principal y recibe la elección del usuario.
    Retorna:
        str: opción seleccionada por el usuario.
    """
    print("\n--- Menú ---")
    print("1. Realizar un nuevo cálculo")
    print("2. Salir")

    while True:
        opcion = input("Seleccione una opción (1-2): ")
        if opcion in ['1', '2']:
            return opcion
        else:
            print("Opción inválida. Intente de nuevo.")

def main():
    """
    Función principal que controla el flujo del programa.
    """
    print("=== Programa para calcular la resta (primer número menos segundo número) ===")

    while True:
        # Entrada de datos
        numero1 = pedir_numero("Ingrese el primer número: ")
        numero2 = pedir_numero("Ingrese el segundo número: ")

        # Procesamiento
        resultado = calcular_resta(numero1, numero2)

        # Salida
        print(f"\nEl resultado de restar {numero2} a {numero1} es: {resultado}")

        # Menú para decidir qué hacer después
        opcion = mostrar_menu()
        if opcion == '2':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
