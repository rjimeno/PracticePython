#!/usr/bin/env python3

a = [5, 10, 15, 20, 25]

def listHas(orderedList, number):
    return number in set(orderedList)

f = open('file.txt', 'w')
if listHas(a, 1):
    f.write("1 is in a.")
else:
    f.write("1 is NOT in a.")


