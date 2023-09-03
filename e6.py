#!/usr/bin/env python3

# CHANGLOG:
# + 20230902:
# - Created and used a reusable function.

def is_palindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    return False

if "__main__" == __name__:
    print("Give me a string and I will check if it is a palindrome: ")
    s = input("Type here: ")
    if is_palindrome(s):
        print("A palindrome!")
    else:
        print("Not a palindrome.")
