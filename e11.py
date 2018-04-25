#!/usr/bin/env python3

def yes(number):
    print("{} is a prime number!".format(number))
    exit(0)

def no(number):
    print("{} is NOT a prime number".format(number))
    exit(0)

number = input("Provide me with a positive integer: ").strip()

try:
    number = int(number)
except ValueError:
    exit(1)

if number <= 0:
    print("That's not a positive integer!")
    exit(1)

if 0 < number < 4:
    yes(number)
    
if 4 == number: 
    no(number)
    
for n in range(2, int(number/2)):
    if 0 == number%n:
        no(number)
    else:
        continue

yes(number)

