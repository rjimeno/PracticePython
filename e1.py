#!/usr/bin/env python3

import datetime

name = input("What's your name?: ")
age = int(input("What's your age?: "))

todayYear=int(datetime.datetime.now().strftime("%Y"))

togo=100-int(age)

print("{}, you will become 100 years old in the year {}.".format(name, todayYear + togo))



