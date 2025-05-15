# En python los bucles son _for_, _in_
# Esto es una variable que en cada vuelta va a ser igual al pedacito
# de variable que estamos igualando
# Todo lo que estamos viendo sirve exactamente igual para tuplas y listas
# Esto no funciona en conjuntos set()

animales = ["pez", "perro", "gato", "loro", "cocodrilo"]
numeros = [20, 40, 28, 98, 34]

for animal in animales:
    print(f"Ahora la varaible animal es igual a: {animal}")

# Recorriendo la lista de números y multiplicado cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

# Iterando dos listas del mismo tamño al mismo timepo.
for numero, animal in zip(animales, numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")

# Forma no optima de recorrer una lista con su índice
for num in range(len(numeros)):
    print(num)

# Forma correcta de recorrer una lista con su índice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El índice es: {indice} y el valor es: {valor}")

# Usando el else, "else", siempre se ejecuta al final del bucle
for numero in numeros:
    print(f"Ejecutando el último bucle, valor actual {numero}")
else:
    print("El bucle termino")
