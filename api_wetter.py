
import requests

# Die URL der API, an die du die Anfrage senden möchtest
url = "https://api.openweathermap.org/data/2.5/weather"
# Deine Parameter, die du in der Anfrage senden möchtest (z.B. Stadtname und API-Schlüssel)
params = {
    #'id': '804',
    #'q': 'Bern',
    #'zip': '8003,ch',
    'lon': 8.5161, 'lat': 47.3726,
    'country': 'CH',
    'appid': '36f6fb7f9e7ccd907a53d12f751e6e8a'
}

# Senden der GET-Anfrage
response = requests.get(url, params=params)

data = response.json()
print(data)
