import oauth
from flask import request
import spotipy


def home():
    return oauth.htmlforloginbutton()


def top_played(accesstoken):
    sp = spotipy.Spotify(accesstoken)
    user = sp.current_user()
    short_term = sp.current_user_top_artists(limit=50, offset=0, time_range='short_term')
    short_term_results = short_term['items']

    short_html = ''

    b = 0
    for name in short_term_results:
        short_html += '<h4>' + str(b + 1) + ". " + short_term_results[b]['name']
        b = b+1

    medium_term = sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')
    medium_term_results = medium_term['items']

    medium_html = ''

    a = 0
    for name in medium_term_results:
        medium_html += '<h4>' + str(a + 1) + ". " + medium_term_results[a]['name']
        a = a+1


    long_term = sp.current_user_top_artists(limit=50, offset=0, time_range='long_term')
    long_term_results = long_term['items']

    long_html = ''

    c = 0
    for name in long_term_results:
        long_html += '<h4>' + str(c + 1) + '. ' + long_term_results[c]['name']
        c = c+1

    site = '<h1>Last 1 week:</br>' + short_html + '<h1>Last 6 months:</br>' + medium_html + '<h1>Last 5 Years:</br>' + long_html
    print(user)
    print(user['display_name'] + " - " + user['email'] + " - " +user['birthdate'])
    return site


def callback():
    url = request.url
    return oauth.callbackauthtoken(url)
