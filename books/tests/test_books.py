from books.requests.books import *

class TestBooks:

    def test_get_books_200(self):
        r = get_books()
        assert r.status_code == 200, 'Status code is not OK'

    def test_get_books_invalid_limit(self):
        r = get_books(limit='21')
        assert r.status_code == 400, 'Status code is not OK'
        assert r.json()['error'] == "Invalid value for query parameter 'limit'. Cannot be greater than 20."

    def test_get_books_invalid_type(self):
        r = get_books(book_type='anotherbook')
        assert r.status_code == 400, 'Status code is not OK'
        assert r.json()['error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

    def test_get_all_books(self):
        r = get_books()
        assert len(r.json()) == 6, 'Book total is incorrect'
        for book in r.json():
            assert book['id'] <= len(r.json()) , 'ID not OK incorrect books'

    def test_get_all_books_limit(self):
        r = get_books(limit=3)
        assert len(r.json()) == 3, 'Total books limit returned is incorrect'

    def test_get_all_books_type_fiction(self):
        r = get_books(book_type='fiction')
        assert len(r.json()) == 4, 'Type fiction returned is incorrect'

    def test_get_all_books_type_non_fiction(self):
        r = get_books(book_type='non-fiction')
        assert len(r.json()) == 2, 'Type non-fiction returned is incorrect'

    def test_get_all_books_type_and_limit(self):
        r = get_books(limit='2',book_type='fiction')
        assert len(r.json()) == 2, 'Total books limit returned is incorrect'
        for book in r.json():
            assert book['type'] == 'fiction', 'Book type returned is not correct'

    def test_get_book_invalid_id(self):
        number_id = 31
        r = get_book(id=number_id)
        assert r.status_code == 404,'status code is not ok'
        assert r.json()['error'] == f'No book with id {number_id}', 'Wrong error message returned'

    def test_get_book_valid_id(self):
        r = get_book(id=6)
        expected_book = {
            "id": 6,
            "name": "Viscount Who Loved Me",
            "author": "Julia Quinn",
            "type": "fiction",
            "price": 15.6,
            "current-stock": 1021,
            "available": True
        }
        assert r.status_code == 200, 'Status code is not OK'
        assert r.json() == expected_book, 'Response body is not correct'
