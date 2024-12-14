#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Name: mystery_6.py
Author: Aseel Omer
Created on: 9 Dec
"""
# --- before documenting and testing 

#def mystery_6(a, b):
#if a == 0:
# return []
#c = []
#while len(c) < a:
# c.append(b)
#b = b + 1
#return c

# --- after documenting and testing 

def mystery_6(a, b):
    """
    Generates a list of integers starting from `b` and of length `a`.

    Args:
        a (int): The number of integers to generate.
        b (int): The starting integer value.

    Returns:
        list: A list containing `a` integers, starting at `b` and incrementing by 1.

    Examples:
        >>> mystery_6(3, 5)
        [5, 6, 7]
        >>> mystery_6(0, 5)
        []
        >>> mystery_6(1, 10)
        [10]
    """
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
