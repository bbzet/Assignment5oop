from tablet import Tablet
import unittest

class TestTablet(unittest.TestCase):
    def test_browse_internet(self):
        tablet = Tablet('Test tablet', 100, 10, 12, '1920x1080', 0.5)
        self.assertEqual(tablet.browse_internet(), 'Browsing the internet')

    def test_use_touch_screen(self):
        tablet = Tablet('Test tablet', 100, 10, 12, '1920x1080', 0.5)
        self.assertEqual(tablet.use_touch_screen(), 'Using the touch screen')
