#!/usr/bin/env python3

import random

length = int(input("How many characters in the password?: ").strip())

characters = []
while 0 <= length:
    length -= 1
    n = random.randint(33, 128)
    characters.append(chr(n))

password = "".join(characters)

print(password)
