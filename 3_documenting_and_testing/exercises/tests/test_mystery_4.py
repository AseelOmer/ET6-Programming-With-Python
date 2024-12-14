import unittest

from ..mystery_4 import mystery_4

class TestMystery4(unittest.TestCase):
    """ """
    def test_zero(self):
        self.assertEqual(mystery_4(0), [])

    def test_positive_numbers(self):
        self.assertEqual(mystery_4(3), [0, 1, 2])
        self.assertEqual(mystery_4(5), [0, 1, 2, 3, 4])
