import unittest

from ..mystery_7 import mystery_7

class TestMystery7(unittest.TestCase):
    """Unit tests for the mystery_7 function."""

    def test_substring_found(self):
        self.assertEqual(
            mystery_7(["apple", "banana", "cherry", "apricot"], "ap"),
            ["apple", "apricot"]
        )

    def test_substring_not_found(self):
        self.assertEqual(mystery_7(["dog", "cat", "rabbit"], "fish"), [])

    def test_empty_list(self):
        self.assertEqual(mystery_7([], "test"), [])

    def test_partial_match(self):
        self.assertEqual(
            mystery_7(["hello", "world", "help", "hold"], "hel"),
            ["hello", "help"])
