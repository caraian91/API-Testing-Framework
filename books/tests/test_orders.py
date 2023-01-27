from books.requests.orders import *
from books.requests.api_clients import *

class TestOrders:
    def setup_method(self):
        self.token = get_token()

    def test_add_valid_order(self):
        r = add_order(self.token, 1, 'Cristian')
        assert r.status_code == 201, 'Status code is not OK'
        assert r.json()['created'] == True, 'Order was not created'
        # cleanup
        delete_order(self.token, r.json()['orderId'])

    def test_add_order_book_out_of_stock(self):
        r = add_order(self.token, 2, 'Cristian')
        assert r.status_code == 404, 'Status code is not OK'
        assert r.json()['error'] == 'This book is not in stock. Try again later.'

    def test_get_all_orders(self):
        add1 = add_order(self.token, 1, 'Eminescu')
        add2 = add_order(self.token, 3, 'Creanga')
        r = get_all_order(self.token)
        assert r.status_code == 200, 'Status code is not OK'
        assert len(r.json()) == 2 , 'Total of orders returned is not correct'
        #cleanup
        delete_order(self.token, add1.json()['orderId'])
        delete_order(self.token, add2.json()['orderId'])

    def test_delete_order(self):
        add = add_order(self.token, 1, 'Caragiale')
        r = delete_order(self.token, add.json()['orderId'])
        assert r.status_code == 204 , 'Status code is not OK'
        # extra check
        get_orders = get_all_order(self.token)
        assert len(get_orders.json()) == 0, 'Order was not deleted'

    def test_delete_invalid_order_id(self):
        r = delete_order(self.token, '3434rdasd34')
        assert r.status_code == 404, 'Status code is not OK'
        assert r.json()['error'] == 'No order with id 3434rdasd34.', 'The error returned is not correct'

    def test_get_one_order(self):
        id = add_order(self.token, 1, 'User1').json()['orderId']
        r = get_one_order(self.token, id)
        assert  r.status_code == 200, 'Status code is not OK'
        # extra check
        assert r.json()['id'] == id, 'id is not OK'
        assert r.json()['bookId'] == 1, 'bookId is not OK'
        assert r.json()['customerName'] == 'User1', 'customerName is not OK'
        assert r.json()['quantity'] == 1, 'quantity is not OK'
        # cleanup
        delete_order(self.token, id)

    def test_get_order_invalid_id(self):
        r = get_one_order(self.token, 'abc123abc')
        assert r.status_code == 404, 'Status code is not OK'
        assert r.json()['error'] == 'No order with id abc123abc.', 'The error returned is not correct'

    def test_patch_invalid_order_id(self):
        r = edit_order(self.token, '123abc', 'Alex')
        assert r.status_code == 404, 'Status code is not OK'
        assert r.json()['error'] == 'No order with id 123abc.', 'The error returned is not correct'

    def test_edit_order_id(self):
        id = add_order(self.token, 1, 'Cristi').json()['orderId']
        r = edit_order(self.token, id, 'Ade')
        assert r.status_code == 204, 'Status code is not OK'
        get = get_one_order(self.token, id)
        assert get.json()['customerName'] == 'Ade', 'Customer name was not updated'
        #cleanup
        delete_order(self.token,id)