# Creando una lista (se puede modificar)
lista = ["Andrés", "desarrollador", "Road to Data", True]

# Creando una tupla (no se puede modificar)
tupla = ("Andrés", "desarrollador", "Road to Data", True)

# Esto es válido
lista[3] = False

# Esto no es válido
# tupla[3] = False

print(lista[2])

# Creando un conjunto (set) (no se accede a elementos
# por indice y no almacena datos duplicados)
conjunto = {"Andrés", "desarrollador", "Road to Data", True}

# print(conjunto[2]) # Esto no es válido,
# ya que no se puede acceder a los elementos por índice

# Creando un diccionario (dict)
diccionario = {
    "nombre": "Andrés",
    "apellido": "Guerrero",
    "edad": 27,
    "trabajo": "desarrollador",
    "empresa": "Road to Data",
    "activo": True,
}
print(diccionario["edad"] + 1)  # Accediendo al valor de la clave 'empresa'
