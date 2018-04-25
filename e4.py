#!/usr/bin/env python3

l = int(input("Would you give me a natural number?: ").strip())

for i in range(1, l+1):
    if l%i==0:
        print("{} is a divisor of {}.".format(i, l))
