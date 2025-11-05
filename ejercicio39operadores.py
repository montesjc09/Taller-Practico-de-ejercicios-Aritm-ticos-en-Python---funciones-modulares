def calcular_promedio(num1, num2):
    """
    Calcula el promedio de dos números.
    Parámetros:
        num1 (float): primer número ingresado.
        num2 (float): segundo número ingresado.
    Retorna:
        float: promedio de los dos números.
    """
    return (num1 + num2) / 2


def mostrar_menu_principal():
    """
    Muestra el menú principal y devuelve la opción elegida.
    Retorna:
        str: opción seleccionada por el usuario.
    """
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Calcular el promedio de dos números")
    print("2. Salir del programa")
    return input("Seleccione una opción: ")


# ---------- FUNCIÓN PRINCIPAL ----------

def ejecutar_programa():
    """
    Controla la ejecución general del programa.
    Permite al usuario realizar cálculos repetidamente o salir.
    """
    while True:
        opcion = mostrar_menu_principal()

        if opcion == '1':
            while True:
                print("\n--- CÁLCULO DEL PROMEDIO ---")
                try:
                    num1 = float(input("Ingrese el primer número: "))
                    num2 = float(input("Ingrese el segundo número: "))

                    promedio = calcular_promedio(num1, num2)

                    print(f"\nEl promedio de {num1} y {num2} es: {promedio:.2f}")
                except ValueError:
                    print("Error: Ingrese solo valores numéricos.")
                    continue

                repetir = input("\n¿Desea calcular otro promedio? (s/n): ").lower()
                if repetir != 's':
                    break

        elif opcion == '2':
            print("\nGracias por usar el programa. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


# ---------- PUNTO DE ENTRADA ----------
if __name__ == "__main__":
    ejecutar_programa()
