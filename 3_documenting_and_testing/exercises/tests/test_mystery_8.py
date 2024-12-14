import unittest

from ..mystery_8 import mystery_8

class TestMystery8(unittest.TestCase):
    """Unit tests for the mystery_8 function."""

    def test_substring_found(self):
        self.assertEqual(
            mystery_8(["apple", "banana", "cherry", "apricot"], "ap"),
            ["apple", "apricot"]
        )

    def test_substring_not_found(self):
        self.assertEqual(mystery_8(["dog", "cat", "rabbit"], "fish"), [])

    def test_empty_list(self):
        self.assertEqual(mystery_8([], "test"), [])

    def test_partial_match(self):
        self.assertEqual(
            mystery_8(["hello", "world", "help", "hold"], "hel"),
            ["hello", "help"]
        )
