#!/usr/bin/env python3

"""
This program used as its original source of data the file available here:
https://raw.githubusercontent.com/alebelcor/celeb-birthdays/master/output/celeb-birthdays.json

BIG THANKS for that file. I the author believes my copying the file is wrong,
I'll delete the file from muy repository.
"""

import json


def load(file):
    '''
    Takes a JSON file (name) as input.
    Output is a data structure that represents the content of the file.
    Side effects: Read the content of the file from storage and populates
    the data structure that will be returned.
    '''
    data = {}
    with open(file, "r") as f:
        date = json.load(f)

    for d in date:
        for name in date[d]:
            data[name]=d
        
    return data


def dump(data, file):
    '''
    Takes a data structure and a file name as input.
    Output: True if the data dump was successful. False otherwise.
    Side effect: creates a file (with the file name) that contains a
    representation of the data structure.
    Side effect: a file is created.
    '''
    try:
        with open(file, "w") as f:
            json.dump(data, f)
    except:
        print("There was a problem dumping data to a file.")
        return False
    return True



def better_birthday_dictionary(b_d):
    '''
    Takes no external input (as everything is defined internally).
    Final output is a message displaying the birthday of someone in the included database.
    Side effect is interaction with the user (input & output) to help him select
    a person's name he might be interested in finding out the birthday.
    '''

    print("Welcome to the birdthday dictionary. We know the birdhdays of:")

    for name in b_d:
        print(name)
    while True:
        name = input("Who's birthday do you want to look up?: ")
        if name in b_d.keys():
            break
        else:
            print("Ups, that's not one of the birthdays I know!")
            print("Please check you typed the name exactly as it appears above.")
            continue

    print(name + "'s birthday is " + b_d[name])

if __name__ == '__main__':
    data = {}
    print('Program is being run by itself.')
    data = load("celeb-birthdays.json")
    dump(data, "celeb-birthdays-output.json")
    better_birthday_dictionary(data)
else:
    print('Functions are being imported from another module.')
