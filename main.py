from asyncio.windows_events import NULL
from pickle import TRUE
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config as config
import urllib.request
from functions import(
    get_user_playlists,
    getNextTracks,
    most_poppin_playlist,
    getTrackKey
)

#defines scope of what program can access in spotify API and gets authentication token
scope = ["playlist-modify-public", "playlist-modify-private", "playlist-read-private", "user-library-modify", "user-read-currently-playing"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_ID, client_secret= config.client_SECRET, redirect_uri=config.redirect_url, scope=scope))

def main():
    #Gets currently playing song's key info
    # try:
    currTrackID = sp.current_user_playing_track()['item']['id']
    currTrackName = sp.current_user_playing_track()['item']['name']
    currKey, mode = getTrackKey(currTrackID)
    print(currTrackName + " is in the key of " + currKey + " " + mode + ".")
    # except TypeError:
    #     print("Error: No song currently playing.")
    #     return 1
    getNextTracks(currTrackID)

if __name__ == '__main__':
    main()
