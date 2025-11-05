def mostrar_menu():
    """
    Muestra el menú principal y solicita la opción al usuario.
    Retorna la opción seleccionada.
    """
    print("--- Menú ---")
    print("1. Calcular producto de dos números")
    print("2. Salir")
    opcion = input("Seleccione una opción (1-2): ")
    return opcion

def solicitar_numero(mensaje):
    """
    Solicita un número al usuario con el mensaje dado.
    Valida que la entrada sea numérica y la devuelve como float.
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

def calcular_producto(num1, num2):
    """
    Calcula el producto de dos números.
    Recibe dos números como parámetros y devuelve su producto.
    """
    return num1 * num2

def preguntar_continuar():
    """
    Pregunta al usuario si desea realizar otro cálculo.
    Devuelve True para continuar, False para salir.
    """
    while True:
        respuesta = input("¿Desea calcular otro producto? (s/n): ").strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Respuesta inválida. Por favor ingrese 's' o 'n'.")

def funcion_principal():
    """
    Función principal que controla el flujo del programa.
    Permite al usuario calcular productos repetidamente o salir.
    """
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            # Entrada
            num1 = solicitar_numero("Ingrese el primer número: ")
            num2 = solicitar_numero("Ingrese el segundo número: ")

            # Procesamiento
            producto = calcular_producto(num1, num2)

            # Salida
            print(f"El producto de {num1} y {num2} es: {producto}\n")

            # Preguntar si desea continuar
            if not preguntar_continuar():
                print("Gracias por usar el programa. ¡Hasta luego!")
                break

        elif opcion == '2':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor seleccione 1 o 2.")

if __name__ == "__main__":
    funcion_principal()
