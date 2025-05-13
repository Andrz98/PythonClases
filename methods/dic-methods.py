"""
ejercicios_diccionarios.py

Colección de ejercicios para practicar métodos y funciones
de manejo de diccionarios en Python:

KEYS()  -> devuelve las claves del diccionario (iterable)
GET()   -> devuelve el valor de una clave, con opción de valor por defecto
CLEAR() -> elimina todos los elementos del diccionario
POP()   -> elimina y devuelve el valor de una clave dada
ITEMS() -> devuelve pares (clave, valor) como tuplas para iterar
"""

marca_modelo = {
    "Mercedez": "AMG",
    "Audi": "A2",
    "Seat": "LEON GTI",
    "Volkswagen": "POLO",
}


# ----------------------------------------
# Ejercicio 1: KEYS()  -> devuelve las claves del diccionario (iterable)
# ----------------------------------------
tipo = marca_modelo.keys()
print(tipo)

# ----------------------------------------
# Ejercicio 2: POP()   -> elimina y devuelve el valor de una clave dada
# ----------------------------------------
modelo_mercedez = marca_modelo.pop("Mercedez")
print("Modelo extraido del Mercedacos:", modelo_mercedez)
print("Dccionario tras el pop('Mercedez'):", marca_modelo)

# ----------------------------------------
# Ejercicio 3: ITEMS() -> devuelve pares (clave, valor) como tuplas para iterar
# ----------------------------------------
item_completo = marca_modelo.items()

print("Me devuelve la clave y el valor:", type(item_completo))
print("Me muestra el contenido del dic de carracos:", item_completo)


# ----------------------------------------
# Ejercicio 4: GET()   -> devuelve el valor de una clave, con opción de
# valor por defecto
# ----------------------------------------
tipo_valor = marca_modelo.get("Audi")
print(tipo_valor)
# ----------------------------------------
# Ejercicio 5: CLEAR() -> elimina todos los elementos del diccionario
# ----------------------------------------
marca_modelo.clear()
print(marca_modelo)
