def calcular_interes(cantidad):
    """
    Calcula el 5% de interés sobre una cantidad de dinero.
    Parámetros:
        cantidad (float): Monto de dinero en la cuenta.
    Retorna:
        float: Interés generado.
    """
    interes = cantidad * 0.05
    return interes

def mostrar_menu_interes():
    """
    Muestra el menú de cálculo de interés y gestiona la interacción del usuario.
    """
    while True:
        print("--- CÁLCULO DE INTERÉS DEL 5% ---")
        try:
            # Paso de ENTRADA
            cantidad = float(input("Ingrese la cantidad de dinero en la cuenta: $"))
            
            # Paso de PROCESAMIENTO
            interes = calcular_interes(cantidad)
            total = cantidad + interes
            
            # Paso de SALIDA
            print(f"\nEl interés generado (5%) es: ${interes:.2f}")
            print(f"El total en la cuenta después del interés es: ${total:.2f}")
        
        except ValueError:
            print("❌ Error: Ingrese un valor numérico válido.")
            continue
        
        # Permitir repetir el cálculo o regresar
        opcion = input("¿Desea realizar otro cálculo de interés? (s/n): ").lower()
        if opcion != "s":
            print("Regresando al menú principal...")
            break


def main():
    """
    Función principal que controla la ejecución del programa.
    Muestra el menú principal y gestiona la navegación del usuario.
    """
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Calcular el 5% de interés sobre una cuenta")
        print("2. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_menu_interes()
        elif opcion == "2":
            print("Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
