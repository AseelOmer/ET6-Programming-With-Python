#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on XX XX XX
@author: Aseel Omer 
"""

# --- before documenting and testing ---

#def mystery_9(a):
    #b = len(a)
    #for c in range(b):
        #for d in range(0, b - c - 1):
            #if a[d] > a[d + 1]:
                #a[d], a[d + 1] = a[d + 1], a[d]
    #return a

#--- after documenting and testing 

def mystery_9(a):
    """
    Sorts a list using bubble sort.

    Args:
        a (list): The list to sort.

    Returns:
        list: The sorted list.

    Examples:
        >>> mystery_9([4, 2, 7, 1, 3])
        [1, 2, 3, 4, 7]
        >>> mystery_9([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
        >>> mystery_9([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
    """
    b = len(a)
    for c in range(b):
        swapped = False
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
                swapped = True
        if not swapped:  # Exit early if no swaps were made
            break
    return a
