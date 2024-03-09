#!/usr/bin/env python3

import datetime as dt

print("This program calculates the year when you will become 100-year old.")

while True:
    name = input("What's your name?: ")
    if 0 < len(name):
        break
while True:
    age_str = input("What's your age in years?: ")
    try:
        age_int = int(age_str)
    except ValueError:
        continue
    if 0 <= age_int:
        break

today_year=int(dt.datetime.now().strftime("%Y"))

left=100-int(age_int)

print(f"{name}, you will become 100 years old in the year {today_year + left}.")
