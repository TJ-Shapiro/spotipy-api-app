import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

##just for syntax highlighting purposes
scope = ["playlist-modify-public", "playlist-modify-private", "playlist-read-private", "user-library-modify", "user-read-currently-playing"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_ID, client_secret= config.client_SECRET, redirect_uri=config.redirect_url, scope=scope))


#returns user's top 10 tracks as a list
def get_user_playlists(sp):
    list = sp.current_user_playlists()
    return list

#Return's playlist with most tracks
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
    
##Gets a track's key and mode (major or minor)
def getTrackKey(trackID):
    pitchKey =sp.audio_analysis(trackID)['track']['key']
    keys = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
    if (sp.audio_analysis(trackID)['track']['mode'] == 1):
        mode = 'Major'
    else:
        mode = 'Minor'
    return keys[pitchKey], mode

def getNextTracks(trackID):
    trackKey = getTrackKey(trackID)
    setlist = sp.playlist_items(sp.current_user_playlists()['items'][1]['id'])

    for idx, track in enumerate(setlist['items']):
        currKey = getTrackKey(track['track']['id'])
        if currKey == trackKey:
            print(track['track']['name'])
    

