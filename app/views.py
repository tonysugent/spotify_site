import oauth
from flask import request

def home():
    return oauth.htmlforloginbutton()



def top_played():
    return 'hi'


def callback():
    url = request.url
    return oauth.callbackauthtoken(url)


