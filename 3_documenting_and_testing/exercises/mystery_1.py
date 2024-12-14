#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Aseel Omer
"""
# --- before documenting and testing 

#def mystery_1(a,b):
    #return a + b

# --- after documenting and testing ---

def mystery_1(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.

    Examples:
    >>> mystery_1(2, 3)
    5

    >>> mystery_1(-1, 10)
    9
    """
    # Ensure both inputs are integers
    assert isinstance(a, int), "The first parameter is not an integer."
    assert isinstance(b, int), "The second parameter is not an integer."
    
    return a + b
