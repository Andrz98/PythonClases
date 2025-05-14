conjunto = set(["Dato 1", "Dato 2"])

# Para introducir un conjunto dentro de otro conjunto, utilizamos frozenset()
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = {conjunto1, "Dato 3"}
print(conjunto2)

print("\n")
print("Teoria de conjuntos")
# Teoria de conjuntos

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {1, 3, 5}

print("Verifico si es un subconjunto")
resultado = conjunto2.issubset(conjunto1)
resultado1 = conjunto2 <= conjunto1
print(resultado)
print(resultado1)

print("\n")
print("Verifico si es un superconjunto")
resultado2 = conjunto1.issuperset(conjunto2)
resultado3 = conjunto1 > conjunto2
print(resultado2)
print(resultado3)

print("\n")
print("Verifico si existe algún número en común")
resultado4 = conjunto2.isdisjoint(conjunto1)
print(resultado4)
