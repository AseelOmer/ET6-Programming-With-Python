import unittest

from ..mystery_1 import mystery_1
class TestMystery1(unittest.TestCase):
    """"""
    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_1(0, 0), 0)
        
    """Unit tests for the mystery_1 function."""

    def test_positive_integers(self):
        self.assertEqual(mystery_1(2, 3), 5) #positive integars

    def test_negative_integers(self):
        self.assertEqual(mystery_1(-1, -9), -10) #negative integars

    def test_zero(self):
        self.assertEqual(mystery_1(0, 7), 7)
        self.assertEqual(mystery_1(0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(AssertionError):
            mystery_1(2, "string")
        with self.assertRaises(AssertionError):
            mystery_1(2.5, 3)
            