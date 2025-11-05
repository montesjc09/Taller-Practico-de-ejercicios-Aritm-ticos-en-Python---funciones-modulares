

# Función que calcula el área de un trapecio
def calcular_area_trapecio(base_mayor, base_menor, altura):
    """
    Calcula el área de un trapecio según la fórmula:
        área = ((base_mayor + base_menor) * altura) / 2
    Parámetros:
        base_mayor (float): longitud de la base mayor del trapecio
        base_menor (float): longitud de la base menor del trapecio
        altura (float): altura del trapecio
    Retorna:
        float: área calculada del trapecio
    """
    area = ((base_mayor + base_menor) * altura) / 2
    return area


# Función que maneja el submenú de cálculos
def menu_calculo_area():
    """
    Muestra el menú de cálculo de área de trapecio.
    Permite al usuario realizar varios cálculos o regresar al menú principal.
    """
    while True:
        print("\n--- CÁLCULO DE ÁREA DE TRAPECIO ---")
        print("1. Calcular área")
        print("2. Regresar al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Paso de ENTRADA
            base_mayor = float(input("Ingrese la longitud de la base mayor: "))
            base_menor = float(input("Ingrese la longitud de la base menor: "))
            altura = float(input("Ingrese la altura del trapecio: "))

            # PROCESAMIENTO: se llama a la función que calcula el área
            area = calcular_area_trapecio(base_mayor, base_menor, altura)

            # SALIDA: mostrar el resultado
            print(f"\nEl área del trapecio es: {area:.2f} unidades cuadradas.")

        elif opcion == "2":
            # Regresa al menú principal
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            continue

        # Pregunta si desea realizar otro cálculo
        repetir = input("\n¿Desea calcular otro trapecio? (s/n): ").lower()
        if repetir != "s":
            break


# Función principal del programa
def main():
    """
    Función principal que controla el flujo general del programa.
    """
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ir al cálculo de área de trapecio")
        print("2. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_calculo_area()
        elif opcion == "2":
            print("Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
