#!/usr/bin/env python3

bd=dict()
bd['BF'] = '01/17/1706'
bd['GH'] = '02/28/1817'

print("Welcome to the birdthday dictionary. We know the birdhdays of:")

for name in bd.keys():
    print(name)

name = input("Who's birthday do you want to look up?: ")

print(name + "'s birthday is " + bd[name])
