#     elif condition:
#     action

ingreso_mensual = 72000
gasto_mensual = 80000

# if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en deficit!")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Lo estás organizando bien... Canalla.")
    else:
        print(
            "Carajo, estás gastando demasiado, controla el bolsillo patrañas"
        )

elif ingreso_mensual > 2000:
    print("Estás bien economicamente en Europa.")

elif ingreso_mensual > 700:
    print("Estás bien en Colombia")

elif ingreso_mensual > 200:
    print("Estás bien en Uganda")

else:
    print("Estás ruinoso.")
