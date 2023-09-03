#!/usr/bin/env python3

# Changelog:
# + 20230902:
# - Reformulated with function so I could exercise a list comprehension.

l = int(input("Would you give me a natural number?: ").strip())

def divisors_of(nn: int) -> list[int]:
    return [d for d in range(1, l+1) if nn%d == 0]

for i in divisors_of(l):
        print("{} is a divisor of {}.".format(i, l))
