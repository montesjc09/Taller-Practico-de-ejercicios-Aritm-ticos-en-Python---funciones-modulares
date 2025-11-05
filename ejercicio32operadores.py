def calcular_area(longitud, ancho):
    area = longitud * ancho
    return area

def mostrar_resultado(longitud, ancho, area):
    print("\n✅ Resultado del cálculo:")
    print(f"Longitud: {longitud} unidades")
    print(f"Ancho: {ancho} unidades")
    print(f"El área del rectángulo es: {area} unidades cuadradas.\n")

def menu_calculo_area():
    while True:
        print("\n--- Cálculo del Área de un Rectángulo ---")
        try:
            longitud = float(input("Ingrese la longitud del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
        except ValueError:
            print("❌ Error: Debe ingresar números válidos.")
            continue

        # Procesamiento
        area = calcular_area(longitud, ancho)

        # Salida
        mostrar_resultado(longitud, ancho, area)

        # Preguntar qué desea hacer
        print("¿Qué desea hacer ahora?")
        print("1. Realizar otro cálculo")
        print("2. Regresar al menú principal")
        print("3. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            continue  # Repite el ciclo
        elif opcion == "2":
            break      # Regresa al menú principal
        elif opcion == "3":
            print(" Gracias por usar el programa. ¡Hasta luego!")
            exit()
        else:
            print(" Opción inválida. Regresando al menú principal.")
            break


def main():
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Calcular el área de un rectángulo")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_calculo_area()
        elif opcion == "2":
            print(" Programa finalizado. ¡Hasta pronto!")
            break
        else:
            print(" Opción no válida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
