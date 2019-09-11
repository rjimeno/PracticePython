#!/usr/bin/env python3

import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = dict()
# This is my initial solution from 20180424.
for x in a:
    if x in set(b):
        c[x]=True
l = list(c.keys())
print(l)


# Extras:
# 1. Randomly generate two lists to test this.

def generate_randomized_list():
    THIS_MAX_INTEGER = 20
    THIS_MAX_LENGTH = 19
    new_list = []
    for i in range(0, THIS_MAX_LENGTH):
        new_list.append(random.randrange(THIS_MAX_INTEGER))
    return new_list

c = generate_randomized_list()
d = generate_randomized_list()

def intersection_as_of_20180424(left, right):
    both = set()
    for x in left:
        if x in set(right):
            both.add(x)
    return both


# Extras:
# 2. Write this in one line of Python (don’t worry if you can’t
# figure this out at this point - we’ll get to it soon)
def intersection(left, right):
    return set(left).intersection(set(right))


print("c == {}".format(c))
print("d == {}".format(d))
inter = intersection(c, d)
print("The intersection of both sets  above is: {}".format(inter))


