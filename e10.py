#!/usr/bin/env python3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [x for x in set(a + b) if x in set(a) and x in set(b)]
print(c)

# Extra: (copied from the Extra solution in e5.py)
# Randomly generate two lists to test this.
def generate_randomized_list():
    THIS_MAX_INTEGER = 20
    THIS_MAX_LENGTH = 19
    new_list = []
    for i in range(0, THIS_MAX_LENGTH):
        new_list.append(random.randrange(THIS_MAX_INTEGER))
    return new_list

a1 = generate_randomized_list()
b1 = generate_randomized_list()

c1 = [x for x in set(a + b) if x in set(a) and x in set(b)]
print("a1 is {}.".format(a1))
print("b1 is {}.".format(b1))
print("Their intersection is is {}.".format(c1))
