#!/usr/bin/env python3
"""
This program used as its original source of data the file available here:
https://raw.githubusercontent.com/alebelcor/celeb-birthdays/master/output/celeb-birthdays.json

BIG THANKS for that file. I the author believes my copying the file is wrong,
I'll delete the file from muy repository.
"""
import json
#from collections import Counter

def load_return_histogram(file_name):
    '''
    Takes a JSON file (name) as input.
    Output is a data structure that represents the content of the file.
    Side effects: Read the content of the file from storage and populates
    the data structure that will be returned.
    '''
    monthly_histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(file_name, "r") as file:
        date = json.load(file)
    for m_d in date:
        tmp = m_d.split('-')
        month = int(tmp[0])-1
        monthly_histogram[month] += len(date[m_d])
    return monthly_histogram


def dump_count(data):
    'Produces JSON output.'

    print("{")
    for month in MONTH:
        print("    '{}': '{}',".format(MONTH[month], data[month]))
    print("}")

if __name__ == '__main__':
    MONTH = {}
    MONTH[0] = 'January'
    MONTH[1] = 'February'
    MONTH[2] = 'March'
    MONTH[3] = 'April'
    MONTH[4] = 'May'
    MONTH[5] = 'June'
    MONTH[6] = 'July'
    MONTH[7] = 'August'
    MONTH[8] = 'September'
    MONTH[9] = 'October'
    MONTH[10] = 'November'
    MONTH[11] = 'December'
    BIRTHDAY_OF = load_return_histogram("celeb-birthdays.json")
    dump_count(BIRTHDAY_OF)
else:
    print('Functions are being imported from another module.')
