import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

#returns user's top 10 tracks as a list
def get_user_playlists(sp):
    list = sp.current_user_playlists()
    return list

def most_poppin_playlist(sp):
    max = 0
    mostpop = " "
    list = get_user_playlists(sp)
    for idx, item in enumerate(list['items']):
        plID = item['id']
        numTracks = len(sp.playlist_items(plID)['items'])
        if numTracks > max and numTracks != 100:
            max = numTracks
            mostpop = item['name']
        print(item['name'] + " has " + str(numTracks) + " tracks")
    print(mostpop + " has the most tracks!")
