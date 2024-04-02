#!/usr/bin/env python3
"""
This program used as its original source of data the file available here:
https://raw.githubusercontent.com/alebelcor/celeb-birthdays/master/output/celeb-birthdays.json

BIG THANKS for that file. I the author believes my copying the file is wrong,
I'll delete the file from muy repository.

Obs.: Lack of unit tests.
"""
import json

def load_return_histogram(file_name):
    '''
    Takes a JSON file (name) as input.
    Output is a data structure that represents the content of the file.
    Side effects: Read the content of the file from storage and populates
    the data structure that will be returned.
    '''
    monthly_histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(file_name, "r", encoding='utf-8') as file:
        date = json.load(file)
    for m_d in date:
        tmp = m_d.split('-')
        month = int(tmp[0])-1
        monthly_histogram[month] += len(date[m_d])
    return monthly_histogram


def dump_count(data):
    'Produces JSON output.'
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    print("{")
    for i, month in enumerate(months):
        print(f"    '{month}': '{data[i]}',")
    print("}")

if __name__ == '__main__':
    BIRTHDAY_OF = load_return_histogram("celeb-birthdays.json")
    dump_count(BIRTHDAY_OF)
else:
    print('Functions are being imported from another module.')
