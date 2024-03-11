#!/usr/bin/env python3

def guessing_game_two():
    """ The computer has to guess a number."""
    print("Think of an integer in the interval [0..100] and write it down.")
    input("Press the Enter key once you are done. ")
    correct = 'no'
    guess = 50
    delta = 50
    while correct != 'yes':
        if guess < 0 or 100 <= guess:
            print("Did you make a mistake above? I detect an error.")
            return
        delta = delta // 2
        delta = max(1, delta)
        s = f"Is it {guess} ? Reply with either 'yes', 'too high' or 'too low': "
        correct = input(s)
        r = str(correct)
        if r == 'too high':
            guess -= delta
        elif r == 'too low':
            guess += delta
        elif r == 'yes':
            print("Great!")
        else:
            print("What?")  

if __name__ == '__main__':
    guessing_game_two()
