#!/usr/bin/env python3

# Changelog:
# + 20240310:
# - Reorganized documentation.
# + 20230902:
# - Created.

"""
Cows And Bulls   
Exercise 18 (and Solution)
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that
the user guessed correctly in the correct place, they have a “cow”. For every digit the user
guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them
how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is
over. Keep track of the number of guesses the user makes throughout teh game and tell the user at
the end.
"""

import random

LENGTH = 4  # Number of digits in the secret (and user-provided) numbers.
#SECRET_NUMBER = "".join([str(random.randint(0,9)) for i in range(4)])
digits = [str(i) for i in range(10)]
SECRET_NUMBER = "".join(random.sample(digits, 4))


def cows(s: str, sn: str = SECRET_NUMBER) -> int:
    """
    >>> cows('1498', '1498')
    4
    """
    c = 0
    for i in range(LENGTH):
        if s[i] == sn[i]:
            c += 1
    return c


def bulls(s: str, sn: str = SECRET_NUMBER) -> int:
    """
    >>> bulls('1234', '1498')
    1
    >>> bulls('1498', '1498')
    0
    >>> bulls('4190', '1498')
    2
    >>> bulls('1498', '4981')
    4
    """
    b = 0
    for i in range(LENGTH):
        if s[i] != sn[i] and s[i] in sn:
            b += 1
    return b

def game(sn: str = SECRET_NUMBER) -> None:
    """
    Additional information (from https://en.wikipedia.org/wiki/Bulls_and_Cows):
    - The digits must be all different.
    """
    print("Welcome to the Cows and Bulls Game!") 
    counter = 0
    while True:
        counter += 1
        while True:
            s = input(f"Enter a number ({LENGTH} unique digits): ").strip()
            if len(s) == len(set(s)):
                break  # all distinct digits.
        c = cows(s, sn)
        b = bulls(s, sn)
        print(f"{c} cows, {b} bulls.")
        if 4 != c:
            continue
        print(f"You guessed it in {counter} attempts!")
        break


if "__main__" == __name__:
    import doctest
    doctest.testmod()  # Provide 'verbose=True' as argument to see test results
    game()