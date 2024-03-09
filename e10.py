#!/usr/bin/env python3

# CHANGELOG:
# + 20230902:
# - Created and used intersection_set_of_two_lists().
# - Reorganized to separate a main function to improve reutilization and testability.

import datetime as dt
from e5 import generate_randomized_list

def intersection_of_two_lists(l_a: list, l_b: list) -> list:
    """
    >>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    >>> b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    >>> intersection_of_two_lists(a, b)
    [1, 2, 3, 5, 8, 13]
    """
    return [x for x in set(l_a).intersection(set(l_b))]
    # return list(set(l_a).intersection(set(l_b)))
    # The forced list comprehension consumes up to 10 % more time.


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    a1 = generate_randomized_list(9999999, 8999999)
    b1 = generate_randomized_list(7999999, 6999999)

    time_before = dt.datetime.now()
    c1 = intersection_of_two_lists(a1, b1)
    time_elapsed = dt.datetime.now() - time_before
    print(f"len(a1) is {len(a1)}.")
    print(f"len(b1) is {len(b1)}.")
    print(f"Their intersection has length {len(c1)}.")
    print(f"Finding the set took this much time: {time_elapsed}.")
