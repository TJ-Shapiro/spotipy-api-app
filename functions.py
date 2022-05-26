import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

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
def getTrackKey(sp, trackID):
    pitchKey =sp.audio_analysis(trackID)['track']['key']
    keys = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
    if (sp.audio_analysis(trackID)['track']['mode'] == 1):
        mode = 'Major'
    else:
        mode = 'Minor'
    return keys[pitchKey], mode

# def printUsefulTrackInfo(sp, trackID):
    

