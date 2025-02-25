from laptop import Laptop
import unittest

class TestLaptop(unittest.TestCase):
    def test_run_program(self):
        laptop = Laptop('Test laptop', 100, 10, 12, 8, 3.4)
        self.assertEqual(laptop.run_program(), 'Running a program')

    def test_use_keyboard(self):
        laptop = Laptop('Test laptop', 100, 10, 12, 8, 3.4)
        self.assertEqual(laptop.use_keyboard(), 'Using the keyboard')