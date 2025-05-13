"""
ejercicios_listas.py

Colección de ejercicios para practicar métodos
y funciones de manejo de listas en Python:

LIST     -> crea una lista
LEN      -> cuenta la cantidad de elementos en una lista

APPEND   -> agrega un elemento al final de la lista
INSERT   -> inserta un elemento en la posición especificada
EXTEND   -> agrega todos los elementos de otro iterable al final

POP      -> elimina y devuelve el elemento en el índice dado
            (por defecto el último)
REMOVE   -> elimina la primera aparición de un valor en la lista
CLEAR    -> elimina todos los elementos de la lista

SORT     -> ordena la lista en orden ascendente (o según key/reverse)
REVERSE  -> invierte el orden de los elementos en la lista
"""

# ----------------------------------------
# Ejercicio 1: Definir Lista y devolver elementos de la lista con len()
# ----------------------------------------

# List() no suele usarse de esta manera, normalmente un buen uso es,
# es una lista vacía, de esta forma podemos guardar información dentro de ella.
lista = list([True, False, 123, "hello"])
print(lista)

conteo_lista = len(lista)
print(conteo_lista)

# ----------------------------------------
# Ejercicio 2: agregar elelentos al final de la lista: append(),
# insertarlo en una posición específica: insert() o
# agregar los elementos a otro iterable extend().
# ----------------------------------------
numeros = []

numeros.append(1)
numeros.append(4)
numeros.append(23)
numeros.append(93)

print("Lista de números:", numeros)
print("Longitud de la lista:", len(numeros))

coches = ["Mercedez", "Audi", "Seat", "VolksWagen"]

coches.insert(
    1,
    "Ferrari",
)
coches.insert(4, "Dacia")
print(coches)

coches.extend(["AMG", "GT", "A2", "LEON GTI", "SANDERO", "POLO"])
print(coches)


# ----------------------------------------
# Ejercicio 3: POP(), elimina y devuelve el elemento en el
# índice dado (por defecto el último)
# ----------------------------------------
frutas = ["Manzana", "Pera", "Platano", "Mandarina"]

frutas.pop()


print("Elemento extraido sin indice:")
print("lista tras popo():", frutas)
# ----------------------------------------
# Ejercicio 4:
# REMOVE   -> elimina la primera aparición de un valor en la lista
# CLEAR    -> elimina todos los elementos de la lista
# ----------------------------------------
modelos_coches = ["AMG", "GT", "A2", "LEON GTI", "SANDERO", "POLO"]

modelos_coches.remove("GT")
print("Se ha eliminado el GT:", modelos_coches)

modelos_coches.clear()
print(modelos_coches)
# ----------------------------------------
# Ejercicio 5:
# SORT     -> ordena la lista en orden ascendente (o según key/reverse)
# REVERSE  -> invierte el orden de los elementos en la lista
# ----------------------------------------
impresoras_3d = [
    "Prusa XL",
    "Bambu Lab",
    "Creality Ender 3 pro",
    "Creality K1C",
]

# Ordeno la lista en orden alfabético
impresoras_3d.sort()
print("He reordenado la lsita por orden alfabético:", impresoras_3d)

# Invierto el orden de la lista
impresoras_3d.reverse()
print("Se cambia el orden de lso modelos de impresoras 3d:", impresoras_3d)
