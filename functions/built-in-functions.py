# Función es un fragmento de código que podemos utilizar en cualquier
# otro momento sin necesidad de volver a crearlo, solo haciendo referencia
# a este. El concepto es igual a lo que hacemos en React con los componentes.

# Encotnrando el número mayor de una lista:
numeros = [1, 4, 7, 9, 24]
numero_mas_alto = max(numeros)
print(numero_mas_alto)

numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# Redondeando a sesis decimales

decimales = round(28.94356, 2)
print(decimales)

# funcición Bool() retorna False -> 0, vacío, false, ninguno
resultado_bool = bool(0)

print(resultado_bool)

# La función All(), retorna True, si todos los valores son veraderos.
resultado_all = all(["true", [344, 23]])
print(resultado_all)

# sum() suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)
