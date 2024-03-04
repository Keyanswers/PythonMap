# Instalación de los paquetes
!pip install matplotlib geopandas

# Importar los paquetes necesarios
import matplotlib.pyplot as plt
import geopandas as gpd

# Mostrar las figuras directamente
%matplotlib inline

# carga los datos geográficos de los países del mundo
NL = gpd.read_file(
    gpd.datasets.get_path('naturalearth_lowres')
)

# Se crea un mapa básico usando GeoPandas y Matplotlib
fig, ax = plt.subplots(figsize=(4, 3))
NL.plot(ax=ax, color='lightgray', edgecolor='black')  # Plotear geometrías
ax.set_xlim([-160.7, -154])  # Ajustar límites del eje x
ax.set_ylim([18.6, 23])      # Ajustar límites del eje y
ax.set_xlabel('Longitud', color='black', size=15)  # Etiqueta del eje x
ax.set_ylabel('Latitud', color='black', size=15)   # Etiqueta del eje y
ax.set_title(r"$\mathrm{Archipiélago\ de\ Hawaii}$")  # Título del mapa
plt.show()

# Instalación del paquete matplotlib-scalebar
!pip install matplotlib-scalebar

# Se importa el paquete ScaleBar desde matplotlib_scalebar
from matplotlib_scalebar.scalebar import ScaleBar

# Se crea un mapa con la escala
fig, ax = plt.subplots(figsize=(4, 3))
NL.plot(ax=ax, color='lightgray', edgecolor='black')  
ax.set_xlim([-160.7, -154])  # Ajusta límites del eje x
ax.set_ylim([18.6, 23])      # Ajusta límites del eje y
ax.set_xlabel('Longitud', color='black', size=15)  # Etiqueta del eje x
ax.set_ylabel('Latitud', color='black', size=15)   # Etiqueta del eje y

# Se incluye la escala en la esquina superior derecha
scalebar = ScaleBar(50, units="km", location='upper right')
ax.add_artist(scalebar)

ax.set_title(r"$\mathrm{Archipiélago\ de\ Hawaii}$")  # Título del mapa
plt.show()

# Importar más bibliotecas necesarias
from matplotlib_scalebar.scalebar import ScaleBar

# Crear un mapa con una señal de norte y la escala
fig, ax = plt.subplots(figsize=(4, 3))
NL.plot(ax=ax, color='lightgray', edgecolor='black')  
ax.set_xlim([-160.7, -154])  # Ajusta límites del eje x
ax.set_ylim([18.6, 23])      # Ajusta límites del eje y
ax.set_xlabel('Longitud', color='black', size=15)  # Etiqueta del eje x
ax.set_ylabel('Latitud', color='black', size=15)   # Etiqueta del eje y

# Añade la flecha que indica el norte y la escala en la esquina superior derecha
x, y, arrow_length = 0.04, 0.99, 0.17
ax.annotate('N', xy=(x, y), xytext=(x, y-arrow_length),
            arrowprops=dict(facecolor='black', width=4, headwidth=13),
            ha='center', va='center', fontsize=12, xycoords=ax.transAxes)

scalebar = ScaleBar(50, units="km", location='upper right')
ax.add_artist(scalebar)

ax.set_title(r"$\mathrm{Archipiélago\ de\ Hawaii}$")  # Título del mapa
plt.show()
