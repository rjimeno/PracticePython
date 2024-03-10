#!/usr/bin/env python3

# Changelog:
# + 20240310:
# - Impleented Pylint advice and reorganized.
# - Added a little documentation.
# - Included a simple performance comparision.

import datetime as dt
from e5 import generate_randomized_list

# lrd() can be implemented either as lrdf() or as lrds(), with the
# latter being faster than the former.
def lrdf(l):
    """ Preserves order but consumes memory and is slow."""
    r=[]
    for i in l:
        if i in r:
            pass
        else:
            r.append(i)
    return r

def lrds(l):
    """ Does not necessarily preserve order."""
    return(list(set(l)))

def lrd(l, preserve_order=False):
    """By default, this function is performant."""
    if preserve_order:
        return lrdf(l)
    return lrds(l)

if __name__ == "__main__":
    assert not lrd([])  # Equivalent to lrd([]) == []
    assert lrd([1]) == [1]
    assert lrd([1, 1]) == [1]
    assert lrd([2, 1, 2]).sort() == [1, 2].sort()

    SIZE = 99999
    RANGE = 9999
    random_integers = generate_randomized_list(SIZE, RANGE)
    time_before = dt.datetime.now()
    no_duplicates = lrd(random_integers, preserve_order=True)
    print(
        f"Preserving order, it took {dt.datetime.now() - time_before}"
        f" to reduce a list of {SIZE} elements to {len(no_duplicates)}"
    )
    time_before = dt.datetime.now()
    no_duplicates = lrd(random_integers)
    print(
        f"Without preserving order, it took {dt.datetime.now() - time_before}"
        f" to reduce a list of {SIZE} elements to {len(no_duplicates)}"
    )

    print(lrd(['a', 'b', 'b', 'c']))
