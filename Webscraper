import requests
from bs4 import BeautifulSoup
import json
import re

# URL der Webseite
url = "http://mainstream.show/konzerte"

# Anfrage an die Webseite
response = requests.get(url)
# HTML-Inhalt der Webseite parsen
soup = BeautifulSoup(response.content, 'html.parser')

# Alle Listenelemente finden
elements = soup.select("#content > article > section > ul > li")

# Liste für strukturierte Daten
structured_data = []

# Daten parsen und strukturieren
for element in elements:
    text = element.get_text()
    
    # Beispieltext: "21.12.24 Chlyklass, Old Capitol, Langenthal"
    # Das Datum ist der erste Teil
    # Der Split erfolgt nach dem ersten Buchstaben
    
    match = re.search(r'([a-zA-Z])', text)
    split_index = match.start(1)
    parts = [text[:split_index].strip(), text[split_index:].strip()]
    date = parts[0] 
    # Falls das Datum aus zwei Daten besteht wird es zusammengesetzt.
    if len(date) > 8: 
        date = date[:3] + date[-5:]
        
    date = date.replace('.', '/')
    # Der Rest ist der zweite Teil   
    rest = parts[1]  
    
    # Weitere Teile durch Komma trennen
    details = rest.split(", ")
    artists = details[0].split(" / ")
    venue = details[1]
    #  location = details[2]
    
    # Strukturierte Daten speichern
    structured_data.append({
        "date": date,
        "artist1": artists[0],
        **{f"artist{i+2}": artist for i, artist in enumerate(artists[1:])},
        "venue": venue,
    #     "location": location
    })

# In JSON umwandeln
json_data = json.dumps(structured_data, ensure_ascii=False, indent=4)

# JSON ausgeben
print(json_data)