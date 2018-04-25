#!/usr/bin/env python3

print("Give me a string and I will check if it is a palindrome: ")
s = input("Type here: ")

for i in range(0, int(len(s)/2)):
    l = len(s)
    if s[i] != s[l-1-i]:
        print("Not a palindrome.")
        exit(1)

print("A palindrome!")
exit(0)