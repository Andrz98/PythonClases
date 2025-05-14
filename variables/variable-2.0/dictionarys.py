# Creando diccionarios con dict()

diccionario = dict(nombre="jalapeños", apellido="romancio", edad="43")

# Las listas no pueden ser claves, lo curioso es que si pueden
# ser tuplas como en este caso:
diccionario = {("jalapeños", "romancios"): "XD"}
print(diccionario)

# En el diccionario si podemos guardar conjuntos, esto lo hacemos mediante
# la función frozenset()
diccionario_1 = {frozenset(diccionario): "XD"}
print(diccionario_1)

# Creamos diccionarios con fromkeys("Dentro de esto, creamos claves")
diccionario_keys = dict.fromkeys("ABCDE")
print(diccionario_keys)

# Lo que hace esto es que cada letra representa el valor de un índice
# del diccionario, esto quiere decir que cada valor es un iterable

# Para que el diccionario provea la lista con un valor con clave "none",
# entonces, solo tenemos que usar: dict.fromkeys([])
diccionario_keys_list = dict.fromkeys(["nombre:", "apellido:"])
print(diccionario_keys_list)
