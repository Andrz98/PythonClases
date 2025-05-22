import pandas as pd

# Usando la función read_csv para leer el archivo CSV
df = pd.read_csv("files-csv\\tareas_aleatorias.csv")
df2 = pd.read_csv("files-csv\\usuarios_emails.csv")


# Obteniendo los datos de la columna nombre
usuarios = df["usuario"]

# Obteniendo el dataframe por la prioridad de forma ascentente
df_orden_ascente = df.sort_values("prioridad")

# Odenar de forma descendente con ascending=false
df_orden_descendente = df.sort_values("prioridad", ascending=False)

# print(df_orden_ascente)
print("========================")
# print(df_orden_descendente)

# Concatenando 2 dataframes

df_concatenado = pd.concat([df, df2])
# print(df_concatenado)

# Accediendo a las 3 filas con head()
primeras_filas = df.head(3)
# print(primeras_filas)

print("========================")
# Accediendo a las 3 últimas filas con tail()
ultimas_filas = df.tail(3)
# print(ultimas_filas)

# accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape
# print(columnas_totales)
# print(filas_totales)

# Obteniendo data estadística del dataframe:
df_info = df.describe()
# print(df_info)

# Accediendo a un elemento específico del df con loc
elemento_específico_loc = df.loc[2, "tarea"]
print(elemento_específico_loc)

# Accediendo a un elemento específico del df con iloc
elemento_específico_iloc = df.iloc[2, 2]
print(elemento_específico_iloc)

# Accediendo a todas las filas de una columna
completadas = df.iloc[:, 3]
print(completadas)

print("=================")
# Accediendo a la fila 3 con loc
fila_3 = df.loc[3, :]
print(fila_3)

print("=================")
# Accediendo a la fila 4 con iloc
fila_4 = df.iloc[4, :]
print(fila_4)

# Accediendoa filas con prioridad True
completadas_True = df.loc[df["completada"] == True, :]
print(completadas_True)
