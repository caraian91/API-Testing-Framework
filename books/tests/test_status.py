from books.requests.status import *

class TestStatus:

    def test_status_200(self):
        assert get_status().status_code == 200, 'Actual status code is not OK'
        assert get_status().json()['status'] == 'OK', 'Actual status message is not OK'