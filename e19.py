#!/usr/bin/env python3

# Changelog:
# + 20230310:
# - Modified (again) because the source changed and didn't work anymore.
# - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
import sys
from bs4 import BeautifulSoup

OK=200
URL='https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'


r = requests.get(URL, timeout=(7, 10))
if r.status_code != OK:
    print("There was a problem with the request.")
    sys.exit(1)

soup = BeautifulSoup(r.text, "html.parser")

content_sections = soup.find_all('a')  # Used to be "class_=content-section"

for t in content_sections:
    print()
    print(t.get('href'))  # Used to be print(t.p)
print()
