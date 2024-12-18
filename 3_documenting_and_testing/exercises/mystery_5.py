#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Name: mystery_5.py
Author: Aseel Omer
Created on: 9 Dec
"""
# --- before documenting and testing 

#def mystery_5(a, b=None):
# # if b is None:
# b = []
#while a:
#c = min(a)
# # a.remove(c)
#b.append(c)
#return b

#--- after documenting and testing 

def mystery_5(a, b):
    """
    Sorts the elements of list `a` in ascending order and appends them to list `b`.

    Args:
        a (list): The list to be sorted.
        b (list, optional): An optional list to which sorted elements will be appended. Defaults to an empty list.

    Returns:
        list: A list containing the sorted elements of `a`, followed by the original elements of `b`.

    Examples:
        >>> mystery_5([3, 1, 2])
        [1, 2, 3]
        >>> mystery_5([4, 2], [1, 3])
        [1, 3, 2, 4]
        >>> mystery_5([])
        []
    """
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
