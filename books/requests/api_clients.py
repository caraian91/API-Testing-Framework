import requests
from random import randint

def login(clientName=None, clientEmail=None):
    body = {
        'clientName': clientName,
        'clientEmail': clientEmail
    }
    r = requests.post('https://simple-books-api.glitch.me/api-clients', json=body)
    return r

def get_token():
    # random numbers (both included)
    nr = randint(1,9999999)
    body = {
        'clientName': 'CRIS',
        'clientEmail': f'email_cristi{nr}@mailinator.com'
    }
    r = requests.post('https://simple-books-api.glitch.me/api-clients', json=body)
    return r.json()['accessToken']