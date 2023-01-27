import requests

def get_books(limit='', book_type=''):
    r = requests.get(f'https://simple-books-api.glitch.me/books?type={book_type}&limit={limit}')
    return r

def get_book(id):
    r = requests.get(f'https://simple-books-api.glitch.me/books/{id}')
    return r