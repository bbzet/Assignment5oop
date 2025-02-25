from cart import Cart
import unittest
from device import Device

class TestCart(unittest.TestCase):
    user1 = Cart()
    device1 = Device('Test device', 100, 10, 12)
    def test_add_device(self):
        self.user1.add_device(self.device1, 5)
        self.assertEqual(self.user1.items, [{'device': self.device1, 'amount': 5}])


    def test_remove_device(self):
        self.user1.add_device(self.device1, 5)
        self.user1.remove_device(self.device1, 5)
        self.assertEqual(self.user1.items, [])

    def test_get_total_price(self):
        self.user1.add_device(self.device1, 5)
        self.assertEqual(self.user1.get_total_price(), 500)

    def test_print_items(self):
        self.user1.add_device(self.device1, 5)
        self.assertEqual(self.user1.items[0]['device'].name, 'Test device')

        print('user1.items:', self.user1.items)

    def test_checkout(self):
        self.user1.add_device(self.device1, 5)
        self.assertEqual(self.user1.checkout(), 'Your total price is 500. Thank you for shopping with us')