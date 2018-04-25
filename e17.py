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

#for story_heading in soup.find_all(class_="story-heading"): 
#    if story_heading.a: 
#        print(story_heading.a.text.replace("\n", " ").strip())
#    else: 
#        print(story_heading.contents[0].strip())
