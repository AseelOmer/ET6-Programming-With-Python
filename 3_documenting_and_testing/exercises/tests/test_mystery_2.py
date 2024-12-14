import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """"""
    def test_empty_list(self):
        self.assertEqual(mystery_2([]), None)
    
    def test_non_empty_list(self):
        self.assertEqual(mystery_2([1, 2, 3]), 3)
        self.assertEqual(mystery_2([1]), 1)
        self.assertEqual(mystery_2([1, 2, 3, 4, 5]), 5)
