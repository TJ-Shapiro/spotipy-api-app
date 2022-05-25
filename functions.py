import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

#returns user's top 10 tracks as a list
def get_user_playlists(sp):
    list = sp.current_user_playlists()
    return list

def most_pop_playlist(userID):
    return " y"
