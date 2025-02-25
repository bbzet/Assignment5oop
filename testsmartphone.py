from smartphone import Smartphone
import unittest

class TestSmartphone(unittest.TestCase):
    def test_make_call(self):
        smartphone = Smartphone('Test smartphone', 100, 10, 12, 5.5, 24)
        self.assertEqual(smartphone.make_call(), 'Making a call')

    def test_install_app(self):
        smartphone = Smartphone('Test smartphone', 100, 10, 12, 5.5, 24)
        self.assertEqual(smartphone.install_app(), 'Installing an app')

