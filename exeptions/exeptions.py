def sumar_dos():

    while True:
        a = input("Número 1: ")
        b = input("Número 2: ")
        try:
            resultado = int(a) + int(b)
        except ValueError as e:
            print("Te pedí un número cojones")
            print(f"ERROR: {e}")
        else:
            break
        finally:
            print("finalally se ejecuta siempre")
    return resultado


print(sumar_dos())
