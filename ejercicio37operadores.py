def verificar_multiplo(numero1, numero2):
    return numero1 % numero2 == 0

def menu_calculos():
    while True:
        print("--- VERIFICADOR DE MÚLTIPLOS ---")

        # Entrada de datos
        try:
            numero1 = int(input("Ingrese el primer número: "))
            numero2 = int(input("Ingrese el segundo número: "))
        except ValueError:
            print(" Error: debe ingresar números enteros válidos.")
            continue

        # Validación de división por cero
        if numero2 == 0:
            print(" No se puede determinar múltiplos con divisor cero.")
            continue

        # Procesamiento (llamada a la función auxiliar)
        es_multiplo = verificar_multiplo(numero1, numero2)

        # Salida (resultado)
        if es_multiplo:
            print(f" El número {numero1} ES múltiplo de {numero2}.")
        else:
            print(f" El número {numero1} NO es múltiplo de {numero2}.")

        # Control de flujo
        print("\n¿Desea realizar otro cálculo?")
        print("1. Sí, otro cálculo")
        print("2. Regresar al menú anterior")
        print("3. Salir del programa")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            continue
        elif opcion == "2":
            break
        elif opcion == "3":
            print(" Gracias por usar el programa.")
            exit()
        else:
            print(" Opción no válida, regresando al menú anterior.")
            break

def main():
    while True:
        print("===============================")
        print("   MENÚ PRINCIPAL DEL PROGRAMA")
        print("===============================")
        print("1. Determinar si un número es múltiplo de otro")
        print("2. Salir")
        print("===============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_calculos()
        elif opcion == "2":
            print(" Saliendo del programa... ¡Hasta pronto!")
            break
        else:
            print(" Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

