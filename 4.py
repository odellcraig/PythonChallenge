#!/usr/bin/env python -w

import re
import requests
next = re.search(r"(\d+)", requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579').text)
while next:
    val = next.group(1)
    response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + val).text
    print val + " -> " + response
    next = re.search(r"(\d+)", response)


# Solution peak.html
# There were several tricks

