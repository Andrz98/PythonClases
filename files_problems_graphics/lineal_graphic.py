import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos el csv correctamente con el pandas pd
df_graphic = pd.read_csv("files_problems_graphics\\ventas_productos.csv")

df_graphic_date = pd.read_csv("files_problems_graphics\\ventas_productos.csv")
# Creo el gráfico con sns de seaborn para prudcto-ventas
sns.lineplot(data=df_graphic, x="producto", y="ventas")

# Mostramos el gráfico con las siguientes categorías:
# Para crear gráficos independientes es importante añadir el método .figure
plt.figure(figsize=(8, 5))  # <- esto es clave!
plt.title("Ventas por producto")
plt.xticks(rotation=45)
plt.tight_layout()


# Creo el gráfico con sns de seaborn para ventas - fecha
sns.lineplot(data=df_graphic_date, x="ventas", y="mes")

# Mostramos el gráfico con las siguientes categorías:
plt.figure(figsize=(8, 5))  # <- esto es clave!
plt.title("venta por mes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Debemos trabajar gráficos de velas, lineales, etc.
