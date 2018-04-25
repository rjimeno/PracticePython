#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

OK=200

r = requests.get('https://www.nyt.com')
if r.status_code != OK:
    print("There was a problem with the request.")
    exit(1)

soup = BeautifulSoup(r.text, "html.parser")

story_headings = soup.find_all(class_="story-heading")

for t in story_headings:
    print(t.a.string)
