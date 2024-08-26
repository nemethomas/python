import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API-Zugangsdaten (von Ihrem Spotify Developer Dashboard)
client_id = ''
client_secret = ''

# Authentifizierung über Client Credentials Flow
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Beispiel: Informationen zu einem Track abrufen
track_id = '3n3Ppam7vgaVa1iaRUc9Lp'  # Track ID für einen bestimmten Song
track = sp.track(track_id)

print(f"Track: {track['name']}")
print(f"Künstler: {track['artists'][0]['name']}")
print(f"Album: {track['album']['name']}")
