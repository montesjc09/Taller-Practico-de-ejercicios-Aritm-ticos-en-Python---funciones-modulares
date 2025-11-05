def calcular_area_paralelogramo(base, altura):
    """
    Calcula el área de un paralelogramo.
    Parámetros:
        base (float): longitud de la base del paralelogramo
        altura (float): altura perpendicular a la base
    Retorna:
        float: área del paralelogramo
    """
    area = base * altura
    return area


# ---------------------- FUNCIÓN DE MENÚ ----------------------

def mostrar_menu_principal():
    """Muestra las opciones principales del programa."""
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Calcular el área de un paralelogramo")
    print("2. Salir")


def manejar_calculo_area_paralelogramo():
    """Controla el flujo del cálculo del área del paralelogramo."""
    while True:
        print("\n--- Cálculo del área de un paralelogramo ---")

        # ENTRADA
        base = float(input("Ingrese la base del paralelogramo: "))
        altura = float(input("Ingrese la altura del paralelogramo: "))

        # PROCESAMIENTO
        area = calcular_area_paralelogramo(base, altura)

        # SALIDA
        print(f"\nResultado: El área del paralelogramo es {area:.2f} unidades cuadradas.")

        # Control del flujo
        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if opcion != 's':
            break


# ---------------------- FUNCIÓN PRINCIPAL ----------------------

def main():
    """
    Función principal del programa.
    Muestra el menú y controla la interacción del usuario.
    """
    while True:
        mostrar_menu_principal()
        opc
