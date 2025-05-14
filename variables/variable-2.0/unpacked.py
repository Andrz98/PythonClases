colores = ("rojo", "verde", "azul", "amarillo")

# Indices
print("Pimero:", colores[0])
print("Segundo:", colores[1])

# Desempaquetado
# a -> Hace referencia al indice [0], ósea al color ["rojo"]
# b -> Hace referencia al indice [1], ósea al color ["verde"]
# c -> Hace referencia al indice [2], ósea al color ["azul"]
# d -> Hace referencia al indice [3], ósea al color ["amarillo"]
a, b, c, d = colores
print(a, b, c, d)

# Conversión en de una lista a una tupla
# 1. Lista de partida
lista = [10, 20, 30, 20, 10]

# 2. Conversión a tupla
t = list([10, 20, 30, 20, 10])

# 3. Contar apariciones del número 20 en la tupla:
veces_20 = t.count(20)
print(
    f"20 aparece: {veces_20} veces",
)

try:
    t[1] = 25
except Exception as e:
    print("Error al modificar tupla:", type(e).t)

# 4. "Modificar" haciendo ida y vuelta
lista2 = list(t)
lista2[1] = 24
t_modificada = tuple(lista2)
print(
    f"""Tupla modificada, se agrego el número 24.
Dando lugar la siguiente lista final: {t_modificada}"""
)
