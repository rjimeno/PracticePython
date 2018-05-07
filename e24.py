#!/usr/bin/env python3

def dashes(s):
    return s * " ---" + " \n"

def bars(s):
    return s * "|   " + "|\n"

def line(s):
    return dashes(s) + bars(s)

def board(s):
    return s * line(s) + dashes(s)

n = input("How many columns (or lines) do you want your square board?: ")
print(board(int(n)))
