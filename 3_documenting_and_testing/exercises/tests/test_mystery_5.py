import unittest

from ..mystery_5 import mystery_5

class TestMystery5(unittest.TestCase):
    """ """

    def test_sorting(self):
        self.assertEqual(mystery_5([3, 1, 2]), [1, 2, 3])

    def test_sorting_with_b(self):
        self.assertEqual(mystery_5([4, 2], [1, 3]), [1, 3, 2, 4])

    def test_empty_a(self):
        self.assertEqual(mystery_5([], [1, 2]), [1, 2])

    def test_empty_a_and_b(self):
        self.assertEqual(mystery_5([]), [])
