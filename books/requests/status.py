import requests

def get_status():
    r = requests.get('https://simple-books-api.glitch.me/status')
    return r