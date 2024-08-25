# Mit diesem Script kann eine beliebige .zip datei aus dem internet heruntergeladen und entpackt werden. 
# Das Download directory ist statisch definiert


import requests
import zipfile
import os

# URL der .zip-Datei
url = "https://data.geo.admin.ch/ch.bakom.mobil-antennenstandorte-lte/data.zip"

# Verzeichnis, in das die Datei heruntergeladen und entpackt wird
download_dir = "/Users/tom/Downloads"

# Dynamischen Dateinamen von der URL ableiten
datei_mit_endung = os.path.basename(url)  
datei_ohne_endung = os.path.splitext(datei_mit_endung)[0] 

# Vollständiger Pfad zur herunterzuladenden ZIP-Datei
local_zip_filename = os.path.join(download_dir, datei_mit_endung)

# Zielverzeichnis zum Entpacken der Dateien (benannt nach dem Dateinamen ohne .zip)
extract_dir = os.path.join(download_dir, datei_ohne_endung)

# Datei herunterladen
response = requests.get(url)
with open(local_zip_filename, 'wb') as file:
    file.write(response.content)


# .zip-Datei entpacken
with zipfile.ZipFile(local_zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)


# .zip-Datei löschen
os.remove(local_zip_filename)

print(f"{datei_ohne_endung} wurde erstellt.")
