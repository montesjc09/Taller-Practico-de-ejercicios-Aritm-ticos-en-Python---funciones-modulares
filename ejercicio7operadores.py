
def mostrar_menu_principal():
    """
    Muestra el menú principal y retorna la opción seleccionada.
    """
    print("=== MENÚ PRINCIPAL ===")
    print("1. Convertir Celsius a Fahrenheit")
    print("2. Salir")
    return input("Seleccione una opción: ")

def solicitar_celsius():
    """
    Solicita al usuario ingresar una temperatura en grados Celsius.
    """
    while True:
        try:
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            return celsius
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def convertir_celsius_a_fahrenheit(celsius):
    """
    Convierte grados Celsius a Fahrenheit.
    Recibe un valor en Celsius y retorna su equivalente en Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def realizar_conversion():
    """
    Controla la operación de conversión e interacción con el usuario.
    Permite repetir la operación o volver al menú principal.
    """
    while True:
        # Paso de entrada
        celsius = solicitar_celsius()

        # Procesamiento
        fahrenheit = convertir_celsius_a_fahrenheit(celsius)

        # Salida
        print(f"{celsius}°C equivale a {fahrenheit:.2f}°F.")

        # Preguntar si desea realizar otra conversión
        repetir = input("¿Desea convertir otra temperatura? (s/n): ").lower()
        if repetir != 's':
            break

def main():
    """
    Función principal que controla el flujo del programa completo.
    """
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            realizar_conversion()
        elif opcion == "2":
            print("Gracias por usar el conversor de temperaturas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
