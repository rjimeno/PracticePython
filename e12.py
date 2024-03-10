#!/usr/bin/env python3

def ht(l):
    """
    >>> ht([5, 10, 15, 20, 25])
    [5, 25]
    """
    return [l[0], l[-1]]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
