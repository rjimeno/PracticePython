#!/usr/bin/env python3

import sys

def rwo(ls):
    """
    >>> rwo("My name is Michele")
    ['Michele', 'is', 'name', 'My']
    """
    words = ls.split()
    words.reverse()
    return words

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    try:
        s = input("Enter the input to be word-reversed: ")
    except Exception as e:
        sys.exit(-1)
    print(" ".join(rwo(s)))
