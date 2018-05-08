#!/usr/bin/env python3

print("Think of an integer in the interval [0..100] and write it down.")
input("Press the Enter key once you are done.")
correct = 'no'
guess = 50
delta = 50
while correct != 'yes':
    delta = delta // 2
    if delta <= 1:
        delta = 1
    s = "Is it {} ? Reply with either 'yes', 'too high' or 'too low': ".format(guess)
    correct = input(s)
    r = str(correct)
    if r == 'too high':
        guess -= delta
    elif r == 'too low':
        guess += delta
    elif r == 'yes':
        print("Great!")
    else:
        print("Really?")
    
            
      
