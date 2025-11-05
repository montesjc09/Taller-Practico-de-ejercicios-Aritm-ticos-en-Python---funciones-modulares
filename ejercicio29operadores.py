def es_par_o_impar(numero):
    """
    Determina si un número es par o impar.
    Retorna 'par' si el número es par, 'impar' si es impar.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"


def main():
    """
    Función principal que solicita un número y muestra si es par o impar.
    """
    try:
        num = int(input("Ingrese un número entero: "))
        resultado = es_par_o_impar(num)
        print(f"El número {num} es {resultado}.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")


if __name__ == "__main__":
    main()
