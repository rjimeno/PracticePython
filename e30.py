#!/usr/bin/env python3

"""
Pick Word http://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
"""
import random

def print_random_word_from(words):
    """
    Takes an array as input and returns the index of one of its elements picked at random.
    As a side-effect it prints the item inidcated by the randomly selected item.
    """
    i = random.randint(0, len(words))
    print("The selected word has index {} and is {}.".format(i, words[i]))
    return i

# Main

WORDS = []
F = open('sowpods.txt', 'r')
LINE = F.readline()
while LINE:
    WORD = LINE.strip()
    WORDS.append(WORD)
    LINE = F.readline()

j = print_random_word_from(WORDS)
