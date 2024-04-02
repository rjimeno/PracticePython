#!/usr/bin/env python3

"""
Pick Word http://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
Obs.: Lack of unit tests.
"""
import random

def load():
    """"
    Loads the sords from swepods.txt into the global words list.
    """
    with open('sowpods.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            word = line.strip()
            words.append(word)
            line = f.readline()

def print_random_word_from(words):
    """
    Takes an array as input and returns the index of one of its
    elements picked at random. As a side-effect it prints the item
    inidcated by the randomly selected index.
    """
    i = random.randint(0, len(words))
    print(f"The selected word has index {i} and is {words[i]}.")
    return i

# Main

words: list[str] = []
load()
j = print_random_word_from(words)
