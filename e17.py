#!/usr/bin/env python3

# Changelog:
# + 20230310:
# - Added timeout to the request.

import requests
import sys
from bs4 import BeautifulSoup

OK=200
URL='https://www.nyt.com'

r = requests.get(URL, timeout=(7, 10))  # https://requests.readthedocs.io/en/latest/user/advanced/#timeouts
if r.status_code != OK:
    print("There was a problem with the request.")
    sys.exit(1)

soup = BeautifulSoup(r.text, "html.parser")

story_headings = soup.find_all(class_="indicate-hover")

for t in story_headings:
    print(t.next)
