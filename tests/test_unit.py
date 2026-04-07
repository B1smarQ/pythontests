import unittest

from main import add_two


class TestUnits(unittest.TestCase):
    def test_addtwo(self):
        a = 2
        b = 2
        self.assertEqual(add_two(a,b),4)

