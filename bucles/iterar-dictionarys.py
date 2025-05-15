persona = {
    "nombre": "Ana",
    "edad": 30,
    "altura": 1.65,
    "estudiante": True,
    "hobbies": ["lectura", "ciclismo", "cine"],
}

# Recorriendo diccionario para obtener las claves
for key in persona:
    key
    print(f"La clave es: {key}")

# Recorriendo diccionario para obtener la clave y el valor
for datos in persona.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es: {value}")
# Recorriendo diccionario para obtener la clave y el valor
