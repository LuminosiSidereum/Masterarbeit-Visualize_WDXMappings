import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #type: ignore
import os
from pathlib import Path
import logging
import time

def visualize_mappings(dateiname: str, element:str):
    """
    Visualizes the mappings of a given element from a CSV file as a heatmap.
    This function reads data from a specified CSV file, determines the value range and colormap 
    based on the provided element, and generates a heatmap visualization. The heatmap is saved 
    as both SVG and PNG files.
    Parameters:
        dateiname (str): The name of the CSV file (without extension) containing the data to be visualized.
        element (str): The element to be visualized. Supported elements are "C", "N", "Fe", and "Zr".
    Raises:
        FileNotFoundError: If the specified CSV file is not found.
        ValueError: If the specified element is not supported.
    Returns:
        None
    """
    
    # CSV-Datei einlesen (ohne Header und Index)
    try:
        data = pd.read_csv(f"data/{dateiname}.csv", header=None).values
    except FileNotFoundError:
        raise FileNotFoundError(f"{Path(__file__).name} line 12: Die Datei {dateiname}.csv wurde nicht gefunden")
    # Wertebereich für das entsprechende Element definieren
    # cmap für das entsprechende Element festlegen
    if element == "C":
        vmin, vmax = 150, 450
        cmap = plt.get_cmap('Greens')
    elif element == "N":
        vmin, vmax = 0, 70
        cmap = plt.get_cmap('Blues')
    elif element == "Fe":
        vmin, vmax = 15, 1100
        cmap = plt.get_cmap('Reds')
    elif element == "Zr":
        vmin, vmax = 2300, 3200
        cmap = plt.get_cmap('Oranges')
    else:
        raise ValueError(f"{Path(__file__).name} line 17+: Das Element *{element}*, welches in *{dateiname}.csv* angegeben ist, ist nicht bekannt.")

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
    print(f"Visualisierung für {dateiname} ({element}) wurde erstellt.")

def setup_output_directories()->None:
    """
    Creates output directories if they do not already exist.
    This function checks for the existence of the directories "svg-output" 
    and "png-output" in the current working directory. If they do not exist, 
    it creates them.
    Returns:
        None
    """
    
    # Erstelle Ausgabeordner, falls sie noch nicht existieren
    for directory in ["svg-output", "png-output"]:
        os.makedirs(directory, exist_ok=True)
        
def main()->int:
    """
    Main function to visualize mappings from CSV files in the 'data' directory.
    This function lists all files in the 'data' directory, filters for CSV files,
    and calls the `visualize_mappings` function for each CSV file found. It counts
    the number of CSV files processed and returns this count.
    Raises:
        FileNotFoundError: If the 'data' directory does not exist.
    Returns:
        int: The number of CSV files processed.
    """
    
    try:
        diretorycontent: list[str] = os.listdir("data") #type: ignore
    except FileNotFoundError:
        raise FileNotFoundError(f"{Path(__file__).name} line 68: Der Ordner 'data' existiert nicht.")
    
    counter: int = 0
    for os_file in diretorycontent:
        file: Path = Path(os_file) #type: ignore
        if file.suffix == ".csv":
            element = file.stem.split("_")[-1]
            visualize_mappings(file.stem, element)
            counter += 1
    return counter
    
if __name__ == "__main__":
    begin = time.perf_counter()
    logging.basicConfig(filename="log_visualizeMappings.log",filemode="a",level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s')
    auswertungsdurchlaeufe = 0
    try:
        setup_output_directories()
        auswertungsdurchlaeufe = main()
    except FileNotFoundError as e:
        logging.error(e)
    except ValueError as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"Ein unbekannter Fehler ist aufgetreten: {e}")
    end = time.perf_counter()
    logging.info(f"Das Programm wurde in {end-begin:.3f} Sekunden ausgefuehrt. Dabei wurden {auswertungsdurchlaeufe} CSV-Dateien visualisiert.")