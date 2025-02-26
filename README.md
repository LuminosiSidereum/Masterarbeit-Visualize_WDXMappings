# WDX Mapping Visualisierung

## Funktionsweise
Dieses Programm erstellt Heatmaps aus den `.csv`-Dateien, die mit dem **WDX CSV Ersteller** generiert wurden.  
Die Visualisierungen werden als `.png` zur direkten Nutzung und als `.svg` zur Weiterverarbeitung in Grafikprogrammen gespeichert.  
Fehlermeldungen und die Laufzeit des Programms werden in der Log-Datei `log_visualizeMappings.log` gespeichert.  

## Nutzung des Skripts
### Eingabedaten
- Das Skript erwartet `.csv`-Dateien im Verzeichnis `data/`.  
- Die Dateien enthalten Messwerte ohne Header oder Index.  
- Der Dateiname muss das zu visualisierende Element enthalten, da dieser für die Skalierung und Farbwahl verwendet wird.  
- Unterstützte Elemente:  
  - **C** → Skalierung: 150–450, Farbe: Grün  
  - **N** → Skalierung: 0–70, Farbe: Blau  
  - **Fe** → Skalierung: 15–1100, Farbe: Rot  
  - **Zr** → Skalierung: 2300–3200, Farbe: Orange  

### Ausführung
1. Stelle sicher, dass sich die `.csv`-Dateien im Ordner `data/` befinden.  
2. Starte das Skript `visualize_mappings.py`.  
3. Das Skript visualisiert alle `.csv`-Dateien und speichert die Ergebnisse.  

### Ausgabe
- **PNG-Dateien** zur direkten Nutzung (`png-output/`).  
- **SVG-Dateien** zur Weiterverarbeitung (`svg-output/`).  
- Die Dateien behalten den Namen der `.csv`-Datei.  