#!/usr/bin/env python3

# CHANGELOG:
# + 20240309:
# -
# + 20230902:
# - More clearly separated __main__ and increase
#   use of functions (not elegantly, though).

import sys

def yes(n: int):
    """
    >>> yes(3)
    3 is a prime number!
    """
    print(f"{n} is a prime number!")

def no(n: int):
    """
    >>> no(4)
    4 is NOT a prime number
    """
    print(f"{n} is NOT a prime number")

def is_prime_number(n: int) -> None:
    """
    >>> is_prime_number(5039)
    5039 is a prime number!
    >>> # is_prime_number(39916801) # May take up to two seconds.
    39916801 is a prime number!
    >>> # is_prime_number(479001599) # May take up to ten seconds.
    479001599 is a prime number!
    """
    if n <= 0:
        print("That's not a positive integer!")
        sys.exit(1)
    if 0 < n < 4:
        yes(n)
        return
    for i in range(2, int(n/2)):
        if 0 == n%i:
            no(n)
            return
    yes(n)

if "__main__" == __name__:
    import doctest
    doctest.testmod()

    number_s = input("Provide me with a positive integer: ").strip()
    try:
        number_i = int(number_s)
    except ValueError:
        sys.exit(1)
    is_prime_number(number_i)