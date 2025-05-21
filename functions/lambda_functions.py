# Creando una función lambda para multiplicar por dos
# multiply_x_dos = lambda x: x * 2

numbers = [1, 2, 3, 4, 5, 10, 20, 34, 58, 7]


# Usando una función building común, que nos devuelva true o false
def is_even(num):
    if num % 2 == 0:
        return True


# Usando filter qué es la función común
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

# Creando lo mismo pero con lambda, pero usado para números impares:
odd_numbers = filter(lambda number: number % 2 == 1, numbers)
print(list(odd_numbers))
