#!/usr/bin/env python3

names = dict()

f = open('names.txt', 'r')

line = f.readline()
while line:
    name = line.strip()
    if name in names.keys():
        pass
    else:
        names[name] = 0
    names[name] += 1
    line = f.readline()

print(names)

