def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    Parámetros:
        base (float): longitud de la base del triángulo
        altura (float): altura del triángulo
    Retorna:
        float: área del triángulo
    """
    area = (base * altura) / 2
    return area

def pedir_numero_positivo(mensaje):
    """
    Solicita al usuario un número positivo.
    Parámetro:
        mensaje (str): texto que se muestra para pedir el dato
    Retorna:
        float: número positivo ingresado por el usuario
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Error: el número debe ser positivo. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

def mostrar_menu_post_calculo():
    """
    Muestra las opciones después de calcular el área para decidir qué hacer.
    Retorna:
        str: opción seleccionada ('1' para repetir, '2' para salir)
    """
    print("¿Qué desea hacer ahora?")
    print("1. Calcular el área de otro triángulo")
    print("2. Salir")
    opcion = input("Seleccione una opción (1-2): ")
    return opcion

def ejecutar_calculo_area_triangulo():
    """
    Función principal que gestiona la interacción con el usuario,
    solicita base y altura, calcula el área y permite repetir o salir.
    """
    while True:
        print("--- Cálculo del área de un triángulo ---")

        base = pedir_numero_positivo("Ingrese la base del triángulo: ")
        altura = pedir_numero_positivo("Ingrese la altura del triángulo: ")

        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")

        opcion = mostrar_menu_post_calculo()

        if opcion == '1':
            continue
        elif opcion == '2':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, saliendo del programa.")
            break

if __name__ == "__main__":
    ejecutar_calculo_area_triangulo()
