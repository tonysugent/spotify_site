import spotipy
from spotipy import oauth2
from flask import request, redirect
from models import User
client_id = '980378f790cb40f595ecebedd58691f8'
client_secret= '365553ea22a64893b758fa2d2f8a79f0'
redirect_uri = "http://127.0.0.1:5000/callback/q"
scope = 'user-read-birthdate, user-read-email, user-top-read'
cache = None

sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope,cache_path=cache)


def htmlforloginbutton():
    auth_url = getspoauthuri()
    htmlloginbutton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlloginbutton


def getspoauthuri():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url


def callbackauthtoken(url):
    print('Access token available! Trying to get user information...')
    code = sp_oauth.parse_response_code(url)
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    sp = spotipy.Spotify(access_token)
    user = sp.current_user()
    user_id = user['id']
    return redirect("/top_played" + "+" + access_token)
    print(user['email'])
    id = user['id']
    firstname, lastname = user['display_name'].split(' ', 1)
    email = user['email']
    User(id, firstname, lastname, email)
