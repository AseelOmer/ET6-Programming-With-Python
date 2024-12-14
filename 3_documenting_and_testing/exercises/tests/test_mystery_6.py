import unittest

from ..mystery_6 import mystery_6

class TestMystery6(unittest.TestCase):
    """ Unit tests for the mystery_6 function."""

    def test_basic_case(self):
        self.assertEqual(mystery_6(3, 5), [5, 6, 7])

    def test_empty_list(self):
        self.assertEqual(mystery_6(0, 5), [])

    def test_single_element(self):
        self.assertEqual(mystery_6(1, 10), [10])

    def test_large_list(self):
        self.assertEqual(mystery_6(5, 1), [1, 2, 3, 4, 5])
