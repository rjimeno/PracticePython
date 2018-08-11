#!/usr/bin/env python3
"""
This program used as its original source of data the file available here:
https://raw.githubusercontent.com/alebelcor/celeb-birthdays/master/output/celeb-birthdays.json

BIG THANKS for that file. I the author believes my copying the file is wrong,
I'll delete the file from muy repository.
"""
import json


def load(file_name):
    '''
    Takes a JSON file (name) as input.
    Output is a data structure that represents the content of the file.
    Side effects: Read the content of the file from storage and populates
    the data structure that will be returned.
    '''
    data = {}
    with open(file_name, "r") as file:
        date = json.load(file)
    for m_d in date:
        month, day = m_d.split('-')
        for name in date[m_d]:
            data[name] = { 'month': month, 'day': day }
    return data


def dump(data, file_name):
    '''
    Takes a data structure and a file name as input.
    Output: True if the data dump was successful. False otherwise.
    Side effect: creates a file (with the file name) that contains a
    representation of the data structure.
    Side effect: a file is created.
    '''
    try:
        with open(file_name, "w") as file:
            json.dump(data, file)
        return True
    except (OSError, IOError) as exception:
        print("There was a problem dumping data to a file: {}.".format(exception))
    return False



def simple_histogram(b_d):
    count_for_month = dict()
    for date in b_d.values():
        month = int(date['month'])
        if month in count_for_month.keys():
            count_for_month[month] += 1
        else:
            count_for_month[month] = 1
    print(count_for_month)
    print("{\n")
    for month in count_for_month.keys():
        print("    \"{}\": \"{}\"\n".format(month, count_for_month[month]))
    print("}\n")

if __name__ == '__main__':
    print('Program is being run by itself.')
    BIRTHDAY_OF = load("celeb-birthdays.json")
    dump(BIRTHDAY_OF, "celeb-birthdays-output.json")
    simple_histogram(BIRTHDAY_OF)
else:
    print('Functions are being imported from another module.')
