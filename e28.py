#!/usr/bin/env python3

values = (1, 2, 3)

def m(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
