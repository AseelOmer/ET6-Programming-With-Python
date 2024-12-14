#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Name: mystery_3.py   
Author: Aseel Omer
Created on: 9 Dec
"""
# ---- before documenting and testing 

#def mystery_4(a):
#  b = []
# c = 0
#while len(b) < a:
#b.append(c)
#c = c + 1
#return b


def mystery_4(a):
    """
    Generate a list of integers from 0 to (a-1).
    
    Args:
        a (int): The length of the list to generate.
    
    Returns:
        list: A list of integers from 0 to a-1.
    
    Examples:
        >>> mystery_4(0)
        []
        >>> mystery_4(3)
        [0, 1, 2]
        >>> mystery_4(5)
        [0, 1, 2, 3, 4]
    """
    b = []
    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1
    return b
