import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import os

# CSV-Datei einlesen (ohne Header und Index)
# Ersetze 'your_data.csv' durch den Pfad deiner Datei
data = pd.read_csv('data/0000-10-06-240927-26_1_N.csv', header=None).values

# Wertebereich definieren
vmin, vmax = 0, 60

# Farbkarte erstellen und Werte außerhalb des Bereichs auf Weiß setzen
cmap = plt.get_cmap('Greens')
cmap.set_under('black')  # Werte unterhalb von vmin
cmap.set_over('black')   # Werte oberhalb von vmax

# Grafikgröße festlegen (z. B. 6x5 Zoll)
figsize = (6, 5)

# Heatmap plotten
fig, ax = plt.subplots(figsize=figsize)
heatmap = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax)

# Farbbalken hinzufügen
cbar = plt.colorbar(heatmap, ax=ax)
cbar.set_label('Probenname')

# Achsenbeschriftungen entfernen (optional)
ax.set_xticks([])
ax.set_yticks([])

# Grafik speichern
plt.tight_layout()
plt.savefig('heatmap_output.svg', format='svg')  # SVG speichern
plt.savefig('heatmap_output.png', format='png', dpi=300)  # PNG speichern
plt.close()

print("Heatmap erfolgreich als SVG und PNG gespeichert.")
