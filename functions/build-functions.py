# Creando una función simple, esta siempre debe de empezar con def()
# def saludar():
#    print("Empezando a crear funciones personalizadas y propias")
#
# Ejecutando la función simple
# saludar()


def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "peeerro"
    else:
        adjetivo = "ni putis"

    print(f"Hola {nombre}, {adjetivo} ¿cómo lo llevas?")


saludar("Amelie", "")
saludar("Jesus", "hombre")
saludar("Ana", "mujer")


# Crear una función que nos retorne multiples valores.
def build_pass_random(num):
    chars = "abcdefjhi"
    int_num = str(num)
    num = int(int_num[0])
    c1 = num - 2
    c2 = num - 1
    c3 = num - 5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return password, num


# Desempaquetando la función
password, first_number = build_pass_random(356)

# Mostrando los reultados

print(f"Ey bandid@ está es tu nueva contraseña: {password}")
print(f"El número que se ha utilziado a sido: {first_number}")
