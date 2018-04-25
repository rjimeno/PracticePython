#!/usr/bin/env python3

import random

min = 1
max = 9

print("I'll select a integer between {} and {} randomly.".format(min, max))

s = random.randint(min, max)

while True:
    g = int(input("Guess which one I picked?: ").strip())
    print("")
    if g < min or max < g:
        continue
    if g < s:
        print("Too LOW, try again.")
        continue
    elif s < g:
        print("Too HIGH, try again.")
        continue
    break

print("You got it! It was number {}.".format(s))
