def mostrar_menu_principal():
    """
    Muestra el menú principal al usuario.
    Devuelve la opción elegida.
    """
    print("----- MENÚ PRINCIPAL -----")
    print("1. Calcular el área de un rectángulo")
    print("2. Salir")
    opcion = input("Seleccione una opción (1-2): ")
    return opcion


def solicitar_dimensiones():
    """
    Solicita la longitud y el ancho del rectángulo al usuario.
    Devuelve los valores como flotantes.
    """
    longitud = float(input("Ingrese la longitud del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    return longitud, ancho


def calcular_area_rectangulo(longitud, ancho):
    """
    Calcula el área de un rectángulo usando la fórmula:
    área = longitud × ancho
    """
    return longitud * ancho


def ejecutar_calculo_area():
    """
    Ejecuta el proceso completo de cálculo del área,
    mostrando resultados y permitiendo repetir, regresar o salir.
    """
    while True:
        print("\n--- CÁLCULO DEL ÁREA DE UN RECTÁNGULO ---")
        
 # Entrada de datos
        longitud, ancho = solicitar_dimensiones()
        
        # Procesamiento
        area = calcular_area_rectangulo(longitud, ancho)
        
        # Salida del resultado
        print(f"El área del rectángulo es: {area}")

        # Opciones siguientes
        print("\n¿Qué desea hacer ahora?")
        print("1. Calcular otra área")
        print("2. Regresar al menú principal")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            continue
        elif opcion == "2":
            break
        elif opcion == "3":
            print("¡Gracias por usar el programa!")
            exit()
        else:
            print("Opción no válida. Regresando al menú principal.")
            break


def ejecutar_programa():
    """
    Función principal que controla el flujo del programa.
    """
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            ejecutar_calculo_area()
        elif opcion == "2":
            print("Programa finalizado. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_programa()
