def calcular_area_cuadrado(lado):
    """Calcula el área de un cuadrado dado su lado."""
    area = lado ** 2
    return area


# -------------------- FUNCIONES DE MENÚ --------------------

def mostrar_menu_principal():
    """Muestra el menú principal y devuelve la opción elegida."""
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Calcular el área de un cuadrado")
    print("2. Salir")
    return input("Elija una opción (1-2): ")

def mostrar_menu_repetir():
    """Muestra el menú de repetición tras realizar un cálculo."""
    print("\n¿Desea realizar otra acción?")
    print("1. Repetir el mismo cálculo")
    print("2. Volver al menú principal")
    print("3. Salir del programa")
    return input("Elija una opción (1-3): ")


# -------------------- FUNCIÓN DE PROCESO --------------------

def ejecutar_calculo_area_cuadrado():
    """Gestiona el flujo de cálculo del área del cuadrado."""
    while True:
        print("\n--- CÁLCULO DEL ÁREA DE UN CUADRADO ---")

        # Entrada de datos
        lado = float(input("Ingrese el valor del lado del cuadrado: "))

        # Procesamiento
        area = calcular_area_cuadrado(lado)

        # Salida del resultado
        print(f"Resultado: El área del cuadrado con lado {lado} es {area:.2f} unidades².")

        # Menú para decidir qué hacer a continuación
        opcion = mostrar_menu_repetir()
        if opcion == "1":
            continue
        elif opcion == "2":
            break
        else:
            salir_programa()


# -------------------- FUNCIÓN DE SALIDA --------------------

def salir_programa():
    """Finaliza el programa de forma controlada."""
    print("\nGracias por usar el programa. ¡Hasta luego!")
    exit()


# -------------------- FUNCIÓN PRINCIPAL --------------------

def main():
    """Función principal que controla el flujo general del programa."""
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            ejecutar_calculo_area_cuadrado()
        elif opcion == "2":
            salir_programa()
        else:
            print("Opción inválida. Intente nuevamente.")


# -------------------- PUNTO DE ENTRADA --------------------

if __name__ == "__main__":
    main()
