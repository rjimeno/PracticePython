#!/usr/bin/env python3

import random

MIN = 1
MAX = 9

print(f"I'll select a integer between {MIN} and {MAX} randomly.")

s = random.randint(MIN, MAX)

while True:
    g = int(input("Guess which one I picked?: ").strip())
    print("")
    if g < MIN or MAX < g:
        continue
    if g < s:
        print("Too LOW, try again.")
        continue
    if s < g:
        print("Too HIGH, try again.")
        continue
    break

print(f"You got it! It was number {s}.")
