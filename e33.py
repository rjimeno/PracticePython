#!/usr/bin/env python3

"""
Defines a single function birthday_dictionary() that takes no output and performs some
standard-input & standard-output operations.
https://www.practicepython.org/solution/2017/02/03/33-birthday-dictionaries-solutions.html
Obs.: Lack of unit tests.
"""

def birthday_dictionary():
    '''
    Takes no external input (as everything is defined internally).
    Final output is a message displaying the birthday of someone in the included database.
    Side effect is interaction with the user (input & output) to help him select
    a person's name he might be interested in finding out the birthday.
    '''
    b_d = {}
    b_d['BF'] = '01/17/1706'
    b_d['GW'] = '02/28/1817'

    print("Welcome to the birdthday dictionary. We know the birdhdays of:")

    for name in b_d:
        print(name)
    while True:
        name = input("Who's birthday do you want to look up?: ")
        if name in b_d:
            break
        print("Ups, that's not one of the birthdays I know!")
        print("Please check you typed the name exactly as it appears above.")

    print(name + "'s birthday is " + b_d[name])

if __name__ == '__main__':
    print('birthday_dictionry() is being run by itself.')
    birthday_dictionary()
else:
    print('birthday_dictionary() is being imported from another module.')
