frutas = ["banana", "platano", "ciriela", "manzana", "pera", "granada"]
cadena = "Qué pasa calabaza?"
numeros = [1, 4, 5, 7, 9]

# Evitando que se coma una manzana con la sentencia "manzana"
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"Me voy a jalar una {fruta}")

print("\n")
# Evitar que el bucle siga ejecutandose (else no se ejecuta)
for fruta in frutas:
    if fruta == "pera":
        break
    print(f"Me voy a jalar una {fruta}")
else:
    print("El bucle acaba aquí")

# Recorrer una cadena de texto
for letra in cadena:
    print(letra)
# for en una sola linea de código
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero * 2)

print(numeros_duplicados)

# for en una sola línea de código, en este caso, siempre etnemos que mantener
# la expresión matemática al principio.
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)
