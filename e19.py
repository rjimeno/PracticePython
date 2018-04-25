#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

OK=200

r = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
if r.status_code != OK:
    print("There was a problem with the request.")
    exit(1)

soup = BeautifulSoup(r.text, "html.parser")

content_sections = soup.find_all(class_="content-section")

for t in content_sections:
    print(t.p)
    print()

