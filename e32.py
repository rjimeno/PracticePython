#!/usr/bin/env python3

"""
Hangman http://www.practicepython.org/exercise/2017/01/10/32-hangman.html
"""
import random

def get_random_word_from(words):
    """
    Takes an array (with words) as input and returns the index of one of its elements
    picked at random.
    """
    return random.randint(0, len(words))

def guess_letters(word):
    """
    Input is a word (as a string).
    Output is zero if the word was not guessed. Otherwise, a positive integer.
    Side effect is interaction with input/output (i.e. guessing the word).
    """
    chances = 6
    tried = ""
    solution = "_" * len(word)
    print(">>> Welcome to Hangman!")
    while 0 < chances:
        print(chances)
        print(solution)
        g_c = input(">>> Guess your letter: ").strip()[0].upper()
        if g_c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            pass
        else:
            continue

        print(solution)
        if g_c in tried:
            print("You tried '{}' before. Try a different one.".format(g_c))
            continue
        else:
            tried = tried + g_c
        if g_c in word:
            pass
        else:
            print(">>> '{}' is not in the word you are trying to guess.".format(g_c))
            chances -= 1
            continue
        tmp = ""
        for w_c in word:
            print(">>>>>> {}.".format(tmp))
            if w_c != g_c:
                tmp += solution[len(tmp)]
            else:
                tmp += w_c
        solution = tmp
    else:
        print(">>> You did not guess all the letters with 6 or fewer guesses.")
        print(">>> The word was: {}.".format(word))
        return 0
    print(solution)
    print(">>> Congratulations, you got the word!")
    return 1

# Main

WORDS = []
F = open('sowpods.txt', 'r')
LINE = F.readline()
while LINE:
    WORD = LINE.strip()
    WORDS.append(WORD)
    LINE = F.readline()

while True:
    j = get_random_word_from(WORDS)
    guess_letters(WORDS[j])
    if 'Y' == input("Would you like to play again? [YN]: ").strip()[0].upper():
        continue
    else:
        break
