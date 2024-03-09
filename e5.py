#!/usr/bin/env python3

import random

# TIME PERFORMANCE COMPARISON:
# Takes under 15 minutes total.
# rjimeno@Mac15 PracticePython % ./e5.py # generate_randomized_list(99999, 99998)
# First: 0:07:06.897740.
# Second: 0:07:16.230384.
# Third: 0:00:00.015316.
# THIS OTHER RUN USES MUCH SMALLER NUMBERS:
# # Takes under 7 seconds total.
# rjimeno@Mac15 PracticePython % ./ e5.py  # generate_randomized_list(9999, 9998)
# First: 0:00:03.476696.
# Second: 0:00:03.411474.
# Third: 0:00:00.001414.


def intersection_before_20180424(a, b):
    """
    >>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    >>> b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    >>> intersection_before_20180424(a, b)
    [1, 2, 3, 5, 8, 13]
    """
    a_and_b = {}
    # This is my initial solution from 20180424.
    for x in a:
        if x in set(b):
            a_and_b[x]=True
    l = list(a_and_b.keys())
    return l

# Extras:
# 1. Randomly generate two lists to test this.

def generate_randomized_list(this_max_integer: int=20, this_max_length: int=19) -> list[int]:
    """
    >>> generate_randomized_list(1,1)
    [0]
    """
    new_list = []
    for _ in range(0, this_max_length):
        new_list.append(random.randrange(this_max_integer))
    return new_list

def intersection_as_of_20180424(left, right):
    """
    >>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    >>> b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    >>> intersection_as_of_20180424(a, b)
    [1, 2, 3, 5, 8, 13]
    """
    both = set()
    for i in left:
        if i in set(right):
            both.add(i)
    return list(both)


# Extras:
# 2. Write this in one line of Python (don’t worry if you can’t
# figure this out at this point - we’ll get to it soon)
def intersection(left, right):
    """
    >>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    >>> b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    >>> intersection_as_of_20180424(a, b)
    [1, 2, 3, 5, 8, 13]
    """
    return list(set(left).intersection(set(right)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    c = generate_randomized_list(999, 999)
    d = generate_randomized_list(999, 999)
    import datetime as dt
    before_first = dt.datetime.now()
    inter_first = intersection_before_20180424(c, d)
    after_first = dt.datetime.now()
    print(f"First: {after_first - before_first}.")

    before_second = dt.datetime.now()
    inter_second = intersection_as_of_20180424(c, d)
    after_second = dt.datetime.now()
    print(f"Second: {after_second - before_second}.")

    before_third = dt.datetime.now()
    inter_third = intersection(c, d)
    after_third = dt.datetime.now()
    print(f"Third: {after_third - before_third}.")

