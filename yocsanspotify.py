import spotipy 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import accesos
#Antes que nada debemos iniciar sesion como developer en spotify 
#Configruacion de los accesos
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id = accesos.SPOTIPY_CLIENT_ID, client_secret=accesos.SPOTIPY_CLIENT_SECRET)

# Play list lo mas escuchado en spotify 2023 Mexico  = 37i9dQZF1DX7K32yYl2HbE o cual quier otro.
playlist_spotify = input('Ingresa el url de la PLAYLIST oobtenida de spotify: \n')

#Colocamos los acceso en una variable
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#separamos la playlist en 2 una que es toda la playlist y otra donde accedemos a las canciones de la playlist
play_list_completa = sp.playlist(playlist_spotify,market='mx')
tracks_in_playlist = sp.playlist_tracks(playlist_spotify, market='mx')

#datos genarales de la playlist
des_playlist = play_list_completa['description']
nombre_playlist = play_list_completa['name']
imagen_playlist = play_list_completa ['images'][0]['url']

# listas donde guardaremos los datos de cada cancion

nombre_cancion = []
duracion_cancion = []
nombre_artista = []
popularidad_track =[]
nombre_album =[]

for track in tracks_in_playlist["items"]:
    nombre_cancion.append(str(track["track"]["name"]))
    duracion_cancion.append(track["track"]["duration_ms"])
    nombre_artista.append(str(track["track"]["artists"][0]["name"]))
    popularidad_track.append(track["track"]["popularity"])
    nombre_album.append(track["track"]["album"]["name"])

#Guardamos el resultado en un dataframe pandas
df = pd.DataFrame({'artista': nombre_artista,'cancion': nombre_cancion,'duracion_cancion':duracion_cancion, 'popularidad': popularidad_track, 'album':nombre_album})
df['minutos_cancion'] = df['duracion_cancion']/60000
print(nombre_playlist, des_playlist, imagen_playlist)
print (df.head())


# imprimir con MATPLOTLIB una grafica de la relacion entre la popularidad de las canciones en la playlist y su duracion en minutos
plt.scatter(df['minutos_cancion'],df['popularidad'])
plt.show()
#descargar la imagen de la playlist


# Pasos para impprimir los la caratula de la playlist.
import requests
from PIL import Image
from io import BytesIO

# URL de la imagen
url = imagen_playlist

# Descargar la imagen desde la URL
response = requests.get(url)
img_data = response.content

# Crear una imagen desde los datos descargados
img = Image.open(BytesIO(img_data))

# Mostrar la imagen
img.show()
#salvalar la imagen descomentar la ultima linea
#img.save('indicar ubicacion de la imagen')

