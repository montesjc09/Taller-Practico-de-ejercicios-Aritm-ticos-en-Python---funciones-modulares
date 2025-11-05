def convertir_horas_a_minutos(horas):
    """
    Recibe una cantidad de horas (float o int) y devuelve
    el equivalente en minutos utilizando operadores aritméticos.
    """
    minutos = horas * 60  # Operación aritmética
    return minutos

def menu_conversion():
    """
    Muestra el menú de conversión y permite repetir o regresar al menú principal.
    """
    while True:
        print("\n--- CONVERSOR DE HORAS A MINUTOS ---")
        try:
            # Entrada
            horas = float(input("Ingrese el número de horas que desea convertir: "))
            
            # Procesamiento
            minutos = convertir_horas_a_minutos(horas)
            
            # Salida
            print(f"\n{horas} hora(s) equivalen a {minutos} minuto(s).")
        
        except ValueError:
            print("Error: debe ingresar un valor numérico válido.")
            continue

        # Preguntar si desea realizar otra conversión
        repetir = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
        if repetir != "s":
            print("Regresando al menú principal...\n")
            break

def main():
    """
    Controla el menú principal del programa y la interacción del usuario.
    """
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Convertir horas a minutos")
        print("2. Salir")

        opcion = input("Seleccione una opción (1-2): ")

        if opcion == "1":
            menu_conversion()
        elif opcion == "2":
            print("Gracias por usar el conversor. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()
