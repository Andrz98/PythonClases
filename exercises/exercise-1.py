# Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# Diferencias de duración (ejercicio A)
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

# Calculando el porcentaje de tiempo vacío removido (ejercicio B)
tiempo_vacio_promedio = (
    100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
)
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10
print("---------------")
# Diferencias de duración (ejercicio A)
print(
    f"""Me muestra la diferencia entre la duración mínima
de los cursos de patraña frenete al cursito de dalto;
dando un total de {diferencia_con_min}% menos que el más rápido.\n """
)
print(
    f"""Me muestra la diferencia entre la duración máxima
de los cursos de patraña frenete al cursito de dalto;
dando un total de {diferencia_con_max}% menos que el más lento.\n"""
)
print(
    f"""Me muestra la diferencia entre la duración mínima
de los cursos de patraña frenete al cursito de dalto;
dando un total de {diferencia_con_promedio}% menos que el promedio.\n"""
)
print("---------------")
# Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)

print(
    f"""Un curso de patraña promedio elimina
{tiempo_vacio_promedio}% de tiempo vacío.\n"""
)
print(f"""Este curso eliminó el {tiempo_vacio_dalto}% de tiempo vacío.\n""")
print("---------------")                                             
# Mostrando diferencias si los cursos duran 10 horas
print(
    f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos.\n"
)
print(
    f"Ver 10 horas de otros cursos equivale a ver{dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso.\n"
)
