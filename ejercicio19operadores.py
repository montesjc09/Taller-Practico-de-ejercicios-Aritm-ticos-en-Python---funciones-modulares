def calcular_volumen_prisma(base, altura, ancho):
    """
    Calcula el volumen de un prisma triangular.
    Parámetros:
        base (float): longitud de la base del triángulo
        altura (float): altura del triángulo
        ancho (float): ancho o profundidad del prisma
    Retorna:
        float: volumen del prisma triangular
    """
    # Paso de procesamiento
    volumen = (base * altura / 2) * ancho
    return volumen


def mostrar_menu_principal():
    """Muestra el menú principal y devuelve la opción elegida."""
    print("====== MENÚ PRINCIPAL ======")
    print("1. Calcular volumen de un prisma triangular")
    print("2. Salir del programa")
    opcion = input("Seleccione una opción (1-2): ")
    return opcion


# ---------------- FUNCIÓN PRINCIPAL -------------------

def main():
    """Función principal que controla el flujo del programa."""
    while True:
        opcion = mostrar_menu_principal()

        if opcion == '1':
            while True:
                print("--- Cálculo del volumen del prisma triangular ---")

                # Paso de ENTRADA
                try:
                    base = float(input("Ingrese la longitud de la base (en cm): "))
                    altura = float(input("Ingrese la altura del triángulo (en cm): "))
                    ancho = float(input("Ingrese el ancho del prisma (en cm): "))
                except ValueError:
                    print("Error: debe ingresar valores numéricos válidos.")
                    continue

                if base <= 0 or altura <= 0 or ancho <= 0:
                    print("Error: todos los valores deben ser positivos.")
                    continue

                # Paso de PROCESAMIENTO
                volumen = calcular_volumen_prisma(base, altura, ancho)

                # Paso de SALIDA
                print(f"\nEl volumen del prisma triangular es: {volumen:.2f} cm³")

                # Control de flujo
                repetir = input("¿Desea realizar otro cálculo? (s/n): ").lower()
                if repetir != 's':
                    break

        elif opcion == '2':
            print("Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# ---------------- EJECUCIÓN DEL PROGRAMA -------------------

if __name__ == "__main__":
    main()
