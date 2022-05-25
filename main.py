from asyncio.windows_events import NULL
from pickle import TRUE
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config as config
import urllib.request
from functions import(
    get_user_playlists,
    most_pop_playlist
)

#defines scope of what program can access in spotify API and gets authentication token
scope = ["playlist-modify-public", "playlist-modify-private", "playlist-read-private", "user-library-modify"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_ID, client_secret= config.client_SECRET, redirect_uri=config.redirect_url, scope=scope))

def main():
    playlists = get_user_playlists(sp)
    for idx, item in enumerate(playlists['items']):
        img = item['images'][0]['url']
        urllib.request.urlretrieve(img, str(idx) + "yup.jpg")
    

if __name__ == '__main__':
    main()
