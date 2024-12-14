#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Name: mystery_3.py
Author: Aseel Omer
Created on: 9 Dec
"""
# --- before documenting and testing 

# def mystery_3(a, b):
#   if a < b:
#      return a
#    elif a > b:
#        return b
#    else:
#        return a + b

# --- after documenting and testing 

def mystery_3(a, b):
    """
    Compares two numbers and returns a value based on their relationship.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: Returns the smaller number if they are not equal. If the numbers are equal, returns their sum.

    Examples:
        >>> mystery_3(2, 3)
        2
        >>> mystery_3(5, 1)
        1
        >>> mystery_3(4, 4)
        8
    """
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
