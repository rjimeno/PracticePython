#!/usr/bin/env python3

"""
Guess Letters http://www.practicepython.org/exercise/2017/01/02/31-guess-letters.htmll
Obs.: Lack of unit tests.
"""

def guess_letters(word):
    """
    Input is a word (as a string). Output is not clearly defined.
    Side effect is interaction with input/output (i.e. guessing the word).
    """
    unknown = len(word)
    solution = "_" * unknown
    print(">>> Welcome to Hangman!")
    while 0 < unknown:
        print(unknown)
        print(solution)
        g_c = input(">>> Guess your letter: ").strip()[0].upper()
        if g_c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            pass
        else:
            continue
        tmp = ""
        for w_c in word:
            if w_c != g_c:
                tmp += solution[len(tmp)]
            elif g_c in solution:
                tmp += w_c
            else:
                tmp += w_c
                unknown -= 1
        solution = tmp
    print(solution)
    print(">>> Congratulations, you got the word!")

guess_letters("EVAPORATE")
