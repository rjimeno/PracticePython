#!/usr/bin/env python3

# Changelog:
# + 20240310:
# - Set (then reset) the random seeed to make randomness testable.
# - Reorganize the code a bit to support a unit test.

import random

def password_generator(size: int) -> str:
    """
    >>> random.seed(0)  # Abritrary seed to make the test predictable.
    >>> print(password_generator(8))
    RV&Bb_TG^
    >>> random.seed()  # DO NOT DELETE! Otherwise, bye-bye randomness!
    """
    characters = []
    while 0 <= size:
        size -= 1
        n = random.randint(33, 128)
        characters.append(chr(n))

    return "".join(characters)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    length = int(input("How many characters in the password?: ").strip())
    # One-line solutions sometimes are difficult to maintain.
    ##password = "".join([chr(random.randint(33, 128)) for n in range(length)])

    print(password_generator(length))
