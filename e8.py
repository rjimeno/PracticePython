#!/usr/bin/env python3

print()
print("Rock Paper Scissors game!")

while True:
    print()
    one = input("What's your move Player One? {R|P|S}: ").strip().upper()[0]
    two = input("What's your move Player Two? {R|P|S}: ").strip().upper()[0]
    print()
    if one == two:
        print("That's a draw, you must chose again!")
        continue

    if one == 'R':
        if two == 'P':
            print("Congratulations Player Two!")
        else:
            print("Congratulations Player One!")

    if one == 'P':
        if two == 'S':
            print("Congratulations Player Two!")
        else:
            print("Congratulations Player One!")
            
    if one == 'S':
        if two == 'R':
            print("Congratulations Player Two!")
        else:
            print("Congratulations Player One!")

    print()
    play_again = input("Would you like to play again? {Y|N}: ").strip().upper()
    if len(play_again) < 1:
        play_again = 'Y'
    if play_again[0] != 'N':
        continue
    else:
        break
