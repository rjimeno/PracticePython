#!/usr/bin/env python3

while True:
    number_str = input("Can I have a natural number please?: ")
    try:
        number = int(number_str)
    except ValueError:
        continue
    if 0 < number:  # Integers smaller than one are not natural numbers.
        break

if (number % 2) == 1:
    print(" oh, that's an odd number!")
else:
    print(" hey, that's an even number!")

