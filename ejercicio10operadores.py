

def calcular_volumen_prisma(longitud, ancho, altura):
    """
    Calcula el volumen de un prisma rectangular.
    Parámetros:
        longitud (float): longitud del prisma
        ancho (float): ancho del prisma
        altura (float): altura del prisma
    Retorna:
        float: volumen calculado del prisma
    """
    volumen = longitud * ancho * altura
    return volumen


def solicitar_datos_prisma():
    """
    Solicita al usuario los datos del prisma rectangular.
    Retorna:
        tuple: contiene longitud, ancho y altura
    """
    print("\n--- INGRESO DE DATOS DEL PRISMA ---")
    longitud = float(input("Ingrese la longitud del prisma: "))
    ancho = float(input("Ingrese el ancho del prisma: "))
    altura = float(input("Ingrese la altura del prisma: "))
    return longitud, ancho, altura


def mostrar_resultado(volumen):
    """
    Muestra el resultado final del cálculo.
    Parámetros:
        volumen (float): volumen calculado del prisma
    """
    print(f"\n>>> El volumen del prisma rectangular es: {volumen:.2f} unidades cúbicas.\n")


# -------------------- FUNCIONES DE CONTROL --------------------

def menu_calculo_prisma():
    """
    Presenta el submenú para calcular el volumen de un prisma rectangular.
    Permite repetir cálculos o regresar al menú principal.
    """
    while True:
        print("--- CÁLCULO DE VOLUMEN DE PRISMA RECTANGULAR ---")
        print("1. Realizar un nuevo cálculo")
        print("2. Regresar al menú principal")
        print("3. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Entrada de datos
            longitud, ancho, altura = solicitar_datos_prisma()
            # Procesamiento
            volumen = calcular_volumen_prisma(longitud, ancho, altura)
            # Salida
            mostrar_resultado(volumen)
        elif opcion == "2":
            print("Regresando al menú principal...\n")
            break
        elif opcion == "3":
            print("Gracias por usar el programa. ¡Hasta pronto!")
            exit()
        else:
            print("Opción inválida. Intente nuevamente.")


def menu_principal():
    """
    Función principal que controla el flujo del programa.
    Presenta el menú general y llama a los submenús correspondientes.
    """
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Calcular volumen de un prisma rectangular")
        print("2. Salir")
        print("===================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_calculo_prisma()
        elif opcion == "2":
            print("Fin del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# -------------------- PUNTO DE ENTRADA --------------------
if __name__ == "__main__":
    menu_principal()
