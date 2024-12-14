#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on XX XX XX
@author: Aseel Omer 
"""

# --- before documenting and testing ---

#def mystery_7(a, b):
    #c = []
    #for d in a:
        #if b in d:
    # c.append(d)
# return c

#---- after documenting and testing

def mystery_7(a, b):
    """
    Filters a list of strings to include only those containing a specific substring.

    Args:
        a (list of str): The list of strings to filter.
        b (str): The substring to search for.

    Returns:
        list of str: A list containing strings from `a` that include `b`.

    Examples:
        >>> mystery_7(["apple", "banana", "cherry", "apricot"], "ap")
        ['apple', 'apricot']
        >>> mystery_7(["dog", "cat", "rabbit"], "fish")
        []
        >>> mystery_7([], "test")
        []
    """
    c = []
    for d in a:
        if b in d:
            c.append(d)
    return c
