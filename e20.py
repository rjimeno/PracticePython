#!/usr/bin/env python3

# Changelog:
# + 20240310:
# - Added search methods (including binary search) and  time comparisions.

import datetime as dt
import random
from e5 import generate_randomized_list

def list_has_1(ordered_list: list[int], number: int) -> bool:
    """
    >>> list_has_1([5, 10, 15, 20, 25], 15)
    True
    """
    return number in ordered_list  # Time complexity is O(n).
    # https://note.nkmk.me/en/python-in-basic/#:~:text=on%20the%20environment.-,Slow%20for%20lists%3A%20O(n),the%20number%20of%20elements%20increases.&text=Execution%20time%20varies%20greatly%20depending,end%20or%20does%20not%20exist.

def list_has_2(ordered_list: list[int], number: int) -> bool:
    """
    >>> list_has_1([5, 10, 15, 20, 25], 15)
    True
    """
    return number in set(ordered_list) # Time complexity is O(1).
    # https://note.nkmk.me/en/python-in-basic/#:~:text=on%20the%20environment.-,Slow%20for%20lists%3A%20O(n),the%20number%20of%20elements%20increases.&text=Execution%20time%20varies%20greatly%20depending,end%20or%20does%20not%20exist.

def list_has_3(ordered_list: list[int], number: int) -> bool:
    """
    >>> list_has_1([5, 10, 15, 20, 25], 1)
    False
    >>> list_has_1([5, 10, 15, 20, 25], 5)
    True
    >>> list_has_1([5, 10, 15, 20, 25], 10)
    True
    >>> list_has_1([5, 10, 15, 20, 25], 15)
    True
    >>> list_has_1([5, 10, 15, 20, 25], 20)
    True
    >>> list_has_1([5, 10, 15, 20, 25], 25)
    True
    >>> list_has_1([5, 10, 15, 20, 25], 30)
    False
    """
    left = 0
    right = len(ordered_list) - 1
    while True:
        middle = right // 2
        if ordered_list[middle] == number:
            return True
        elif ordered_list[left] <= number < ordered_list[middle]:
            right = middle - 1
        elif ordered_list[middle] < number <= ordered_list[right]:
            left = middle + 1
        else:
            return False

def list_has(ordered_list, number, impl=2):
    """ Returns True if 'number' is in 'ordered_list'. """
    if impl == 1:
        list_has_1(ordered_list, number)
    elif impl == 2:
        list_has_2(ordered_list, number)
    list_has_3(ordered_list, number)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    SIZE = 9999999
    RANGE = SIZE
    random_integers = generate_randomized_list(SIZE, RANGE)
    time_before = dt.datetime.now()
    list_has_1(random_integers, 0)
    list_has_1(random_integers, RANGE + 1)
    list_has_1(random_integers, int(RANGE + 1 / 2))
    list_has_1(random_integers, random.randrange(RANGE + 1))
    print(f"Method 1 took {dt.datetime.now() - time_before}"
          ". It conversts a list to a set and checks in O(1).")
    time_before = dt.datetime.now()
    list_has_2(random_integers, 0)
    list_has_2(random_integers, RANGE + 1)
    list_has_2(random_integers, int(RANGE + 1 / 2))
    list_has_2(random_integers, random.randrange(RANGE + 1))
    print(f"Method 2 took {dt.datetime.now() - time_before}"
          ". It performs a linear search in O(n).")
    time_before = dt.datetime.now()
    list_has_3(random_integers, 0)
    list_has_3(random_integers, RANGE + 1)
    list_has_3(random_integers, int(RANGE + 1 / 2))
    list_has_3(random_integers, random.randrange(RANGE + 1))
    print(f"Method 3 took {dt.datetime.now() - time_before}"
          ". When the list is sorted, we can perform binary search in O(log N).")