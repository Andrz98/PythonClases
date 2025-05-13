"""
ejercicios_cadenas.py

Colección de ejercicios para practicar métodos
y funciones de manejo de cadenas en Python:

DIR        -> devuelve la lista de atributos y métodos válidos de un objeto
LEN        -> cuenta los caracteres de una secuencia


UPPER      -> convierte todos los caracteres de una cadena a mayúsculas
LOWER      -> convierte todos los caracteres de una cadena a minúsculas
CAPITALIZE -> pone en mayúscula la primera letra y en minúscula el resto

FIND       -> busca la primera aparición de una subcadena; devuelve índice o -1
INDEX      -> busca la primera aparición de una subcadena;
            devuelve índice o lanza ValueError

ISNUMERIC  -> True si todos los caracteres de la cadena son dígitos numéricos
ISALPHA    -> True si todos los caracteres de la cadena son letras alfabéticas

COUNT      -> cuenta cuántas veces aparece una subcadena dentro de la cadena


ENDSWITH   -> True si la cadena termina con el sufijo dado
STARTSWITH -> True si la cadena empieza con el prefijo dado

REPLACE     -> reemplaza todas (o un número limitado)
            de apariciones de una subcadena
SPLIT      -> divide la cadena en una lista usando el separador dado
"""

# ----------------------------------------
# Ejercicio 1: Listar métodos y atributos
# ----------------------------------------

# Definimos la cadena de la que queremos obtener sus métodos y atributos
texto = "Python Senior"

# Obtenemos la lista de nombres disponibles para el objeto `texto`
metodos = dir(texto)

# Mostramos la lista por pantalla
print("Métodos y atributos disponibles:")
print(metodos)

# Contamos cuántos métodos y atributos hay con la función len()
print("\nNúmero total de métodos/atributos:", len(metodos))


# ----------------------------------------
# Ejercicio 2: Normalizar mayúsculas y minúsculas
# ----------------------------------------

# Cadena de ejemplo para transformar
cadena_pruebas = "hOlA pYtHoN!"

# 1. Convertir todo el texto a MAYÚSCULAS
resultado_upper = cadena_pruebas.upper()
print("\nCadena en mayúsculas:")
print(resultado_upper)

# 2. Convertir todo el texto a minúsculas
resultado_lower = cadena_pruebas.lower()
print("\nCadena en minúsculas:")
print(resultado_lower)

# 3. Poner solo la primera letra en mayúscula y el resto en minúsculas
resultado_capitalize = cadena_pruebas.capitalize()
print("\nCadena capitalizada:")
print(resultado_capitalize)


# ----------------------------------------
# Ejercicio 3: Buscar subcadenas con find() e index()
# ----------------------------------------

# Línea de log para buscar con find()
linea_log = "12-05-2025 23:20:04 - INFO - Conexión establecida correctamente"

# Usamos .find() para buscar la subcadena "INFO"
pos_info = linea_log.find("INFO")

# .find() devuelve -1 si no encuentra la subcadena
if pos_info != -1:
    print(f"\nINFO encontrado en índice {pos_info}")
else:
    print("\nEn este momento la línea no contiene 'INFO'")

# Otra línea de log para buscar con index()
linea_error = (
    "12-05-2025 23:20:04 - ERROR - Conexión establecida correctamente"
)

# .index() lanza ValueError si no encuentra la subcadena
try:
    pos_error = linea_error.index("ERROR")
    print(f"ERROR encontrado en índice {pos_error}")
except ValueError:
    print("En este momento la línea no contiene 'ERROR'")

aparece_num = linea_log.count("2")
print(f"2 aparece {aparece_num} veces")


# ----------------------------------------
# Ejercicio 4: Aprendizaje para distinguir cadenas que contienen solo dígitos
# (isnumeric) de cadenas que contienen solo letras (isalpha)
# ----------------------------------------

valores = ["1234", "Python", "Python3", "-.#~"]

for contenido in valores:
    # Compruebo que "contenido" es totalmente numérico
    es_num = contenido.isnumeric()
    # Compruebo que "contenido" es totalmente alfabético
    es_alpha = contenido.isalpha()

    print(f"{contenido}: isnumeric? {es_num} | isalpha? {es_alpha}")

# ----------------------------------------
# Ejercicio 5: Aprender a comprobar si una cadena empieza o termina
# con un texto concreto
# ----------------------------------------
# Lista de nombres de archivos
archivos = [
    "informe_final.pdf",
    "foto_vacaciones.JPG",
    "datos.csv",
    "reporte.PDF",
    "script.py",
    "documento.docx",
]

# Mediante el bucle for, detecto archivos PDF (sufijo.pdf, sin importar mayus)
for nombre in archivos:
    # Convierto a minúsculas para hacer la busqueda insensible a mayúsculas
    if nombre.lower().endswith(".pdf"):
        print("PDF encontrado:", nombre)

# Ahora lo que busco, es detectar archivos con prefijos script
for nombre in archivos:
    # startwith() si distingue mayúsculas; usamos el name directamente
    if nombre.startswith("script"):
        print("Script encontradísimo:", nombre)

# ----------------------------------------
# Ejercicio 6: Practicar el método replace
# ----------------------------------------

texto = "error, error, error, todo debuti"

# Necesito remplazar todas las ocurrencias de "error" por "todo debuti"
texto_weno = texto.replace("error", "ok")
print("Remplazo total:", texto_weno)

# Y también necesito remplazar solo las dos primeras ocurrencias
texto_parcial = texto.replace("error", "ok", 2)
print("Remplazo limitado", texto_parcial)


# ----------------------------------------
# Ejercicio 6: Practicar el método split
# ----------------------------------------

csv = "Ana,Luis,María,Javier,Pedro"

# 1. Dividir toda la cadena usando coma como serpador
lista_separada = csv.split(",")
print("Lista separada:", lista_separada)

# Dividir solo los nos promeros nombres
lista_parcial = csv.split(",", 2)
print("Lista mas o menos:", lista_parcial)

# Separar por espacios (por defecto) y eliminar espacios extra
espacio_texto = " muchos espacios intermedios"
partes = espacio_texto.split()
print("División por defecto:", partes)
