import unittest
from device import Device
class TestDevice(unittest.TestCase):
    def test_display_info(self):
        device = Device('Test device', 100, 10, 12)
        self.assertEqual(device.display_info(), 'Device name: Test device, Price: 100, Stock: 10, Warranty period: 12')

    def test_apply_discount(self):
        device = Device('Test device', 100, 10, 12)
        self.assertEqual(device.apply_discount(20), 80)

    def test_is_available(self):
        device = Device('Test device', 100, 10, 12)
        self.assertTrue(device.is_available(5))