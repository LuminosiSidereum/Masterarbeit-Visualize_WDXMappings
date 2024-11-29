import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #type: ignore
import os
from pathlib import Path
import logging

def visualize_mappings(dateiname: str, element:str):
    # CSV-Datei einlesen (ohne Header und Index)
    data = pd.read_csv(f"data/{dateiname}.csv", header=None).values

    # Wertebereich für das entsprechende Element definieren
    # cmap für das entsprechende Element festlegen
    if element == "C":
        vmin, vmax = 150, 450
        cmap = plt.get_cmap('Greens')
    elif element == "N":
        vmin, vmax = 0, 60
        cmap = plt.get_cmap('Blues')
    elif element == "Fe":
        vmin, vmax = 15, 1000
        cmap = plt.get_cmap('Reds')
    elif element == "Zr":
        vmin, vmax = 2400, 3200
        cmap = plt.get_cmap('Oranges')

    # Werte außerhalb des Bereichs auf Schwarz setzen
    cmap.set_under('black')  # Werte unterhalb von vmin
    cmap.set_over('black')   # Werte oberhalb von vmax

    # Grafikgröße festlegen
    figsize = (6, 5)

    # Heatmap plotten
    fig, ax = plt.subplots(figsize=figsize)
    heatmap = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax)

    # Farbbalken hinzufügen und anpassen
    cbar = plt.colorbar(heatmap, ax=ax)
    num_ticks: int = 10
    ticks: list[int] = np.linspace(vmin, vmax, num_ticks, dtype=int).tolist()
    cbar.set_ticks(ticks)
    cbar.set_label(label=dateiname)

    # Achsenbeschriftungen entfernen (optional)
    ax.set_xticks([])
    ax.set_yticks([])

    # Grafik speichern
    plt.tight_layout()
    plt.savefig(f"svg-output/{dateiname}.svg", format='svg')  # SVG speichern
    plt.savefig(f"png-output/{dateiname}.png", format='png', dpi=300)  # PNG speichern
    plt.close()

def setup_output_directories():
    # Erstelle Ausgabeordner, falls sie noch nicht existieren
    for directory in ["svg-output", "png-output"]:
        os.makedirs(directory, exist_ok=True)
        
def main():
    try:
        diretorycontent: list[str] = os.listdir("data")
    except FileNotFoundError:
        raise FileNotFoundError("Der Ordner 'data' existiert nicht!")
    
    for os_file in diretorycontent:
        file: Path = Path(os_file)
        if file.suffix == ".csv":
            element = file.stem.split("_")[-1]
            visualize_mappings(file.stem, element)
    
    
if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO)
    # try:
        setup_output_directories()
        main()
    #except FileNotFoundError as e:
    #    logging.error(e)
    # except Exception as e:
    #     logging.error(f"Ein unbekannter Fehler ist aufgetreten! {e}")