#!/usr/bin/env python3

# Changelog:
# + 20230309:
# - Followed Pylint advice on names of constants and variables and f-strings.
# - Stopped using numbers.Number for type hints.
# + 20230902:
# - Added type hints.
# - import sys to prevent the IDE (or linter) from warning.

import sys

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
DEFAULT_LIMIT = 5
for x in a:
    if x < DEFAULT_LIMIT:
        print(x)

# Extras:

# 1.Instead of printing the elements one by one, make a new list that has all
# the elements less than 5 from this list in it and print out this new list.
def list_less_than(input_array: list, limit_int: int=DEFAULT_LIMIT) -> list:
    """
    >>> list_less_than([])
    []
    >>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    >>> list_less_than(a)
    [1, 1, 2, 3]
    >>> list_less_than(a, 8)
    [1, 1, 2, 3, 5]
    """
    l = []
    for n in input_array:
        if n < limit_int:
            l.append(n)
    return l

# 2. Write this in one line of Python.
def list_less_than_oneliner(i_a: list, l: int=DEFAULT_LIMIT) -> list:
    """
    >>> list_less_than([])
    []
    >>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    >>> list_less_than_oneliner(a)
    [1, 1, 2, 3]
    >>> list_less_than_oneliner(a, 8)
    [1, 1, 2, 3, 5]
    """
    return [n for n in i_a if n < l]

try:
    limit = int(input(
        "What's the smallest number you don't care about (i.e. "
        f"What's the limit? Default is {DEFAULT_LIMIT}."
    ))
except Exception as e:
    print(f"That did not look like a number: '{e}'")
    print(f"Will default of {DEFAULT_LIMIT} instead.",
          file=sys.stderr)
    limit = DEFAULT_LIMIT
print(list_less_than_oneliner(a, limit))



if '__main__' == __name__:
    import doctest
    doctest.testmod()
    