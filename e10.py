#!/usr/bin/env python3

# CHANGELOG:
# + 20230902:
# - Created and used intersection_set_of_two_lists().
# - Reorganized to separate a main function to improve reutilization and testability.

from e5 import generate_randomized_list


def intersection_set_of_two_lists(l_a: list, l_b: list) -> set:
    return set([x for x in set(l_a + l_b) if x in set(l_a) and x in set(l_b)])

if __name__ == "__main__":
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    c = intersection_set_of_two_lists(a, b)
    print(c)

    a1 = generate_randomized_list()
    b1 = generate_randomized_list()

    c1 = intersection_set_of_two_lists(a1, b1)
    print("a1 is {}.".format(a1))
    print("b1 is {}.".format(b1))
    print("Their intersection is is {}.".format(c1))
