#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Name: mystery_3.py   
Author: Aseel Omer
Created on: 9 Dec
"""

import unittest

from ..mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):

    """ """
    """ Tests for the mystery_3 function."""

    def test_a_less_than_b(self):
        """It should return a when a < b."""
        self.assertEqual(mystery_3(2, 5), 2)

    def test_a_greater_than_b(self):
        """It should return b when a > b."""
        self.assertEqual(mystery_3(7, 3), 3)

    def test_a_equal_to_b(self):
        """It should return a + b when a == b."""
        self.assertEqual(mystery_3(4, 4), 8) 
