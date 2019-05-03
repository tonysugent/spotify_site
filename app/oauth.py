from spotipy import oauth2
from flask import request
client_id = '980378f790cb40f595ecebedd58691f8'
client_secret= '365553ea22a64893b758fa2d2f8a79f0'
redirect_uri = "http://apitestforfun.ddns.net"
scope = 'user-read-birthdate, user-read-email, user-top-read'
cache = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope,cache_path=cache)

def authorize():

    access_token = ""
    token_info = sp_oauth.get_cached_token()

    if token_info:

        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)

        if code:

            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print('Access token available! Trying to get user information...')
        global sp
        sp = spotipy.Spotify(access_token)
        results = sp.current_user()
        return mid()
    else:
        return htmlforloginbutton()

def htmlforloginbutton():
    auth_url = getspoauthuri()
    htmlloginbutton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlloginbutton

def getspoauthuri():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url