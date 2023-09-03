#!/usr/bin/env python3

import random

length = int(input("How many characters in the password?: ").strip())
# One-line solutions sometimes are difficult to maintain.
##password = "".join([chr(random.randint(33, 128)) for n in range(length)])

characters = []
while 0 <= length:
    length -= 1
    n = random.randint(33, 128)
    characters.append(chr(n))

password = "".join(characters)

print(password)
