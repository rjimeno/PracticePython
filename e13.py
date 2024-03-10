#!/usr/bin/env python3

# Changelog:
# + 20240310:
# - Error and exception handling.
# - Reorganized as functions with unit tests.

import sys

def nth_fib(n):
    """
    >>> nth_fib(1)
    0
    >>> nth_fib(2)
    1
    >>> nth_fib(3)
    1
    >>> nth_fib(4)
    2
    """
    if n < 1:
        sys.exit(n)
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib(n - 2) + nth_fib(n - 1)
    
def fib_sequ_of_n(n):
    """
    >>> fib_sequ_of_n(0)
    []
    >>> fib_sequ_of_n(3)
    [0, 1, 1]
    >>> fib_sequ_of_n(7)
    [0, 1, 1, 2, 3, 5, 8]
    """
    result=[]
    for i in range(1, n + 1):
        result.append(nth_fib(i))
    print(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    try:
        length = int(input("How many Fibonacci numbers?: "))
    except ValueError:
        sys.exit(-1)  # $? is 255
    fib_sequ_of_n(length)
