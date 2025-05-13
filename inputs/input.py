# Input, se utiliza para leer texto desde la entradad estándar
# (normalmente el teclado) y devolverlo como una cadena.
# Es fundamenteal para interactuar con el usuario en un programa de consola.

"""
La sintaxis básica de input es:
variable = input(prompt) -> el prompt es simplemente opcional, pero
muestra el mensaje que verá el usuario en su consola.
"""

nombre = input("Dime tu pinche nombre bandido!:")

"""
Para los números, input funciona de una manera distinta, puesto que debemos
entender que el valor que estamos recibiendo debe pasarse de str a int o float.
"""
edad_str = input("Y, cuanto años tienes mendrugo? ")
edad = int(edad_str)

resultado = float(edad) * 2
print(
    f"""Te ponemos unos años de más, porque
    sabemos que mientes más que hablas ¡animal!.
    Tu edad real es de {resultado} años, pedazo de bandido""",
)

if resultado < 18:
    print(f"Eres un siverguenza, vete pa casa {nombre}.")
elif 18 <= resultado < 30:
    print(f"Tienes la edad suficiente para ser un garrulo {nombre}.")
elif resultado <= 30:
    print(f"Deja de salir de fiesta y ponte a trabajar {nombre}!")
else:
    print(
        f"""Estás empezando a chochear
        vuelvete pa tu casa que te caes...{nombre}"""
    )

caja_informacion = list([nombre, edad])
print(f"El nombre y la edad que dice el bicho: {caja_informacion}")
