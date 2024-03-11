#!/usr/bin/env python3

from e20 import list_has

a = [5, 10, 15, 20, 25]

with open('file.txt', 'w', encoding="utf-8") as f:
    if list_has(a, 1):
        f.write("1 is in a.")
    else:
        f.write("1 is NOT in a.")
