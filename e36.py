#!/usr/bin/env python3
"""
This program used as its original source of data the file available here:
https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

https://raw.githubusercontent.com/alebelcor/celeb-birthdays/master/output/celeb-birthdays.json
BIG THANKS for that file. I the author believes my copying the file is wrong,
I'll delete the file from muy repository.

Obs.: Lack of unit tests.
"""
import json
from bokeh.plotting import figure, show, output_file

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

if __name__ == '__main__':
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    output_file("plot.html")
    BIRTHDAY_OF = load_return_histogram("celeb-birthdays.json")
    p = figure(x_range=months)
    p.vbar(x=[i for i in range(len(months))], top=BIRTHDAY_OF, width=0.5)
    show(p)
else:
    print('Functions are being imported from another module.')
