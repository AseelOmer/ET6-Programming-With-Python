#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on XX XX XX
@author: Aseel Omer 
"""

# --- before documenting and testing ---

#def mystery_8(a, b):
    #while a:
        #if b in a[0]:
            #c.append(a[0])
        #return c

# --- after docuemting and testing

def mystery_8(a, b):
    """
    Filters a list of strings to include only those containing a specific substring.

    Args:
        a (list of str): The list of strings to filter.
        b (str): The substring to search for.

    Returns:
        list of str: A list containing strings from `a` that include `b`.

    Examples:
        >>> mystery_8(["apple", "banana", "cherry", "apricot"], "ap")
        ['apple', 'apricot']
        >>> mystery_8(["dog", "cat", "rabbit"], "fish")
        []
        >>> mystery_8([], "test")
        []
        >>> mystery_8(["hello", "world", "help", "hold"], "hel")
        ['hello', 'help']
    """
    return [item for item in a if b in item]
