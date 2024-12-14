#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on XX XX XX
@author: Aseel Omer 
"""

# --- before documenting and testing ---



#def mystery_2(a):
    #if len(a) == 0:
        #return None
# return len(a)

#--- after documenting and testing 

def mystery_2(a):
    """
    Returns the length of the input list, or None if the list is empty.

    >>> mystery_2([1, 2, 3])
    3
    >>> mystery_2([])
    None
    """
    if len(a) == 0:
        return None
    return len(a)
