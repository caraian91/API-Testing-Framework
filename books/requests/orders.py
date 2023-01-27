import requests
from requests.structures import CaseInsensitiveDict

def add_order(token, bookId, customerName):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    body = {
        'bookId': bookId,
        'customerName': customerName
    }
    r = requests.post('https://simple-books-api.glitch.me/orders', headers=headers, json=body)
    return r

def delete_order(token, order_id):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    r = requests.delete(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=headers)
    return r

def get_one_order(token, order_id):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    r = requests.get(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=headers)
    return r

def get_all_order(token):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    r = requests.get(f'https://simple-books-api.glitch.me/orders', headers=headers)
    return r

def edit_order(token, order_id, customerName):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    body = {
        'customerName': customerName
    }
    r = requests.patch(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=headers, json=body)
    return r