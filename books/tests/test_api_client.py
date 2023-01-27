from books.requests.api_clients import *

class TestApiClient:
    nr = randint(1, 9999999)
    clientName = 'CRIS'
    clientEmail = f'email_cristi{nr}@mailinator.com'

    def setup_method(self):
        self.r = login(self.clientName, self.clientEmail)

    def test_succesful_login(self):
        assert self.r.status_code == 201, 'Actual status code is not correct'
        assert 'accessToken' in self.r.json().keys(), 'Token property is not present in the response'

    def test_login_409(self):
        self.r = login(self.clientName, self.clientEmail)
        assert self.r.status_code == 409, 'Status code is not OK'
        assert self.r.json()['error'] == 'API client already registered. Try a different email.'

    def test_invalid_email(self):
        self.r = login('Cris', '')
        assert self.r.status_code == 400, 'Status code is not OK'
        assert self.r.json()['error'] == 'Invalid or missing client email.'

    def test_invalid_name(self):
        self.r = login('','email_cristi@mailinator.com')
        assert self.r.status_code == 400, 'Status code is not OK'
        assert self.r.json()['error'] == 'Invalid or missing client name.'
