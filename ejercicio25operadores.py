def solicitar_numero(mensaje):
    """
    Solicita al usuario un número decimal.
    Parámetros:
        mensaje (str): mensaje para pedir el número.
    Retorna:
        float: número válido ingresado por el usuario.
    """
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def calcular_division(dividendo, divisor):
    """
    Calcula la división entre dos números.
    Parámetros:
        dividendo (float): número que se divide.
        divisor (float): número divisor.
    Retorna:
        float: resultado de la división si es válida.
        None: si el divisor es cero.
    """
    if divisor == 0:
        return None
    return dividendo / divisor

def mostrar_menu():
    """
    Muestra el menú para decidir continuar, regresar o salir.
    Retorna:
        str: opción seleccionada ('1', '2', '3').
    """
    print("\n¿Qué desea hacer ahora?")
    print("1. Realizar otra división")
    print("2. Regresar al menú principal")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")
    return opcion

def main():
    """
    Función principal que controla el flujo del programa.
    """
    while True:
        print("\n=== División de dos números ===")
        num1 = solicitar_numero("Ingrese el primer número (dividendo): ")
        num2 = solicitar_numero("Ingrese el segundo número (divisor): ")

        resultado = calcular_division(num1, num2)
        if resultado is None:
            print("Error: No se puede dividir entre cero.")
        else:
            print(f"El resultado de dividir {num1} entre {num2} es: {resultado}")

        opcion = mostrar_menu()
        if opcion == '1':
            # Repetir cálculo sin volver al menú principal
            continue
        elif opcion == '2':
            # Regresar al inicio (en este caso es lo mismo que repetir, porque no hay menú adicional)
            continue
        elif opcion == '3':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Saliendo del programa.")
            break

if __name__ == "__main__":
    main()
