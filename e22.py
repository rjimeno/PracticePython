#!/usr/bin/env python3

names = {}

with open('names.txt', 'r',  encoding="utf-8") as f:
    line = f.readline()
    while line:
        name = line.strip()
        if name in names:
            pass
        else:
            names[name] = 0
        names[name] += 1
        line = f.readline()
print(names)
