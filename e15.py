#!/usr/bin/env python3

long_string = "My name is Michele"

def rwo(ls):
    words = ls.split()
    words.reverse()        
    return words

print(rwo(long_string))
