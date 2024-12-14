import unittest

from ..mystery_9 import mystery_9

class TestMystery9(unittest.TestCase):
    """Unit tests for the mystery_9 function."""

    def test_unsorted_list(self):
        self.assertEqual(mystery_9([4, 2, 7, 1, 3]), [1, 2, 3, 4, 7])

    def test_sorted_list(self):
        self.assertEqual(mystery_9([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_order(self):
        self.assertEqual(mystery_9([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_mixed_strings(self):
        self.assertEqual(mystery_9(["banana", "apple", "cherry"]), ["apple", "banana", "cherry"])

    def test_empty_list(self):
        self.assertEqual(mystery_9([]), [])

    def test_single_element(self):
        self.assertEqual(mystery_9([1]), [1])
