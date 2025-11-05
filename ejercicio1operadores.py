

# ---------------------------------------------
# Función principal que inicia el programa
# ---------------------------------------------
def ejecutar_programa():
    while True:
        opcion = mostrar_menu_principal()

        if opcion == '1':
            iniciar_calculo_area()
        elif opcion == '2':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor seleccione 1 o 2.")


# ---------------------------------------------
# Muestra el menú principal al usuario
# ---------------------------------------------
def mostrar_menu_principal():
    print("======= MENÚ PRINCIPAL =======")
    print("1. Calcular área de un triángulo")
    print("2. Salir")
    return input("Seleccione una opción: ")


# ---------------------------------------------
# Inicia el flujo para calcular área de triángulo
# ---------------------------------------------
def iniciar_calculo_area():
    while True:
        print("--- CÁLCULO DE ÁREA DE TRIÁNGULO ---")

        base = pedir_valor_positivo("Ingrese la base del triángulo: ")
        altura = pedir_valor_positivo("Ingrese la altura del triángulo: ")

        area = calcular_area_triangulo(base, altura)

        print(f"El área del triángulo con base {base} y altura {altura} es: {area:.2f} unidades cuadradas")

        if not preguntar_repeticion():
            break  # Volver al menú principal


# ---------------------------------------------
# Calcula el área de un triángulo
# Fórmula: (base * altura) / 2
# ---------------------------------------------
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


# ---------------------------------------------
# Solicita al usuario un número positivo
# ---------------------------------------------
def pedir_valor_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print(" El valor debe ser mayor que cero.")
        except ValueError:
            print(" Entrada inválida. Por favor, ingrese un número válido.")


# ---------------------------------------------
# Pregunta al usuario si desea repetir el cálculo
# ---------------------------------------------
def preguntar_repeticion():
    while True:
        respuesta = input("¿Desea calcular otra área? (s/n): ").strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print(" Respuesta no válida. Ingrese 's' para sí o 'n' para no.")


# ---------------------------------------------
# Punto de entrada del programa
# ---------------------------------------------
if __name__ == "__main__":
 ejecutar_programa()