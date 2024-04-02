#!/usr/bin/env python3

"""
Hangman http://www.practicepython.org/exercise/2017/01/10/32-hangman.html
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
        print(solution)
        if word == solution:
            break
        g_c = input(">>> Guess your letter: ").strip()[0].upper()
        if g_c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            pass
        else:
            continue
        if g_c in tried:
            print(f"You tried '{g_c}' before. Try a different one.")
            continue
        tried = tried + g_c
        if g_c in word:
            pass
        else:
            print(f"'{g_c}' is not in the word you are trying to guess.")
            chances -= 1
            print(f"You have {chances} missed guesses left!")
            continue
        tmp = ""
        for w_c in word:
            if w_c != g_c:
                tmp += solution[len(tmp)]
            else:
                tmp += w_c
        solution = tmp
    else:
        print("You did not guess all the letters with 6 or fewer wrong guesses.")
        print(f"The word was: {word}.")
        return 0
    print("Congratulations, you got the word!")
    return 1

# Main

words: list[str] = []
load()

while True:
    j = get_random_word_from(words)
    guess_letters(words[j])
    if 'Y' == input(">>> Would you like to play again? [YN]: ").strip()[0].upper():
        continue
    break
