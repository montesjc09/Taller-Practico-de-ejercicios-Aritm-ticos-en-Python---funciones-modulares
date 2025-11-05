
def calcular_volumen_cubo(lado):
    volumen = lado ** 3  # Fórmula del volumen del cubo
    return volumen

def solicitar_lado():
    while True:
        try:
            lado = float(input("Ingrese la longitud del lado del cubo (en unidades): "))
            if lado <= 0:
                print(" El valor debe ser mayor que cero. Intente nuevamente.")
                continue
            return lado
        except ValueError:
            print(" Error: Ingrese un número válido.")

def realizar_calculo_volumen():
    while True:
        print("\n===== CÁLCULO DEL VOLUMEN DE UN CUBO =====")
        lado = solicitar_lado()  # Entrada
        volumen = calcular_volumen_cubo(lado)  # Procesamiento
        print(f"El volumen del cubo con lado {lado} es: {volumen} unidades cúbicas.")  # Salida

        # Preguntar si desea repetir
        continuar = input("\n¿Desea calcular otro volumen? (s/n): ").lower()
        if continuar != 's':
            break


def mostrar_menu_principal():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Calcular volumen de un cubo")
    print("2. Salir")
    print("===========================")


def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-2): ")

        if opcion == '1':
            realizar_calculo_volumen()
        elif opcion == '2':
            print(" Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print(" Opción no válida. Intente nuevamente.")


# ------------------------------------------------------------
# Punto de entrada del programa
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
