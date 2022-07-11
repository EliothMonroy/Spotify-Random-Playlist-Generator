# Libraries
import os
import pprint
from random import randint

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Enviromental variables
os.environ["SPOTIPY_CLIENT_ID"] = ""
os.environ["SPOTIPY_CLIENT_SECRET"] = ""
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost/"

scope = 'user-library-read playlist-modify-public'

playlist_id = ''

track_ids = []

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# The number of tracks that you have in your library (not needed to be the exact amount)
library_size = 9800

# The number of tracks that you want in your playlist
number_tracks_playlist = 50

for i in range(number_tracks_playlist):

    ran = randint(0, library_size)

    result = sp.current_user_saved_tracks(limit=1, offset=ran)
    for item in result['items']:
        track = item['track']
        track_ids.append(track['id'])

results = sp.playlist_replace_items(playlist_id, track_ids)
pprint.pprint(results)
