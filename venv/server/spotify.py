import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# def sign_in(self, username=None):
def sign_in(username=None):
    token = util.prompt_for_user_token(username, scope='user-modify-playback-state',
                                       client_id='e6201d58d3cf4a32a59f88274a5f3d23',
                                       client_secret='61470390772a4b18a618f940fcb5a602',
                                       redirect_uri='http://localhost/')
    sp = spotipy.Spotify(auth=token)
    return sp

def play():
    print()

sp = sign_in('mateomeoteo')
sp.start_playback(context_uri='spotify:user:sam17marchant:playlist:5tNZUmEQ8Aa50cbrNBwKhW')

# username = 'mateomeoteo'
# token = util.prompt_for_user_token(username, scope='user-modify-playback-state',
#                                     client_id='e6201d58d3cf4a32a59f88274a5f3d23',
#                                     client_secret='61470390772a4b18a618f940fcb5a602',
#                                     redirect_uri='http://localhost/')
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# sp = spotipy.Spotify(auth=token)
# playlists = sp.user_playlists('sam17marchant')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
# print(sp.user_playlist_tracks('sam17marchant', 'spotify:user:sam17marchant:playlist:5tNZUmEQ8Aa50cbrNBwKhW'))
# sp._put(url='https://api.spotify.com/v1/me/player/play', context_uri='spotify:user:sam17marchant:playlist:5tNZUmEQ8Aa50cbrNBwKhW', offset='{"position": 0}')
# sp.start_playback(context_uri='spotify:user:sam17marchant:playlist:5tNZUmEQ8Aa50cbrNBwKhW')


