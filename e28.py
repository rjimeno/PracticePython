#!/usr/bin/env python3

"Finds the largest of three numbers without using max()"

def m(a, b, c):
    """
    >>> m(1, 2, 3)
    3
    >>> m(1, 3, 2)
    3
    >>> m(2, 1, 3)
    3
    >>> m(2, 3, 1)
    3
    >>> m(3, 1, 2)
    3
    >>> m(3, 2, 1)
    3
    >>> m(1, 1, 2)
    2
    >>> m(1, 2, 1)
    2
    >>> m(2, 1, 1)
    2
    >>> m(1, 1, 1)
    1
    """
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c

if __name__ == "__main__":
    import doctest
    doctest.testmod()
