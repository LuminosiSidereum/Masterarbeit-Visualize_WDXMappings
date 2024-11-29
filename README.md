# Masterarbeit-Visualize_WDXMappings
## What does the program do?
Creates heatmaps of the wdx mapping data, saved as csv-files in the data directory, and stores them as png and svg.
The svg-files can be further modivied using Inkscape or CorelDraw.

The latest file, which was saved as png and svg, is shown on the terminal.

The errors as well as the runtime of the program are logged in the logilfe: `log_viszualieMappings.log`

## How to interact with the program
1. Create csv-files which contain only the values for each pixel of the heatmap (not header or index)
2. Properly name the csv-filse, because the name of the csv-file will appear in the png and the heatmaps will be named like the csv as well.
3. Put all the csv-files into the `data` directory
4. Run `visualize_mappings.py`
5. After completion of the skript, you will find the heatmaps in the subdirctories `png-output` and `svg-output`  