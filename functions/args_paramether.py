# Forma no optima de sumar valores ->
#  - ⤵️
# def suma(list):
#     added_nums = 0
#     for number in list:
#         added_nums = added_nums + number
#     return added_nums
# resultado = suma([5, 3, 9, 10, 20, 3])


# 🛡️ Forma óptima de sumar valores
def total_sum(numbers):
    return [*numbers]


result1 = total_sum([5, 3, 9, 10, 20, 3])


# Forma correcta y clara de usar *args para sumar
def sumar_numeros(nombre, *numeros):
    """
    Suma los valores recibidos como argumentos variables.

    Args:
        nombre (str): Nombre que se mostrará en el mensaje.
        *numeros (int): Una cantidad variable de números a sumar.

    Returns:
        str: Mensaje con el nombre y la suma total.
    """
    total = sum(numeros)  # Aquí sí usamos la función interna sum correctamente
    return f"{nombre}, la suma de los números te da: {total}"


resultado = sumar_numeros("Bandido", 5, 3, 9, 10, 20, 3)
print(resultado)
