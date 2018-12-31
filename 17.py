#!/usr/bin/env python -w

import bz2
import re
import requests
import urllib

response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345')
print(response.text)
next = re.search(r"(\d{2,})", response.text)
first = response.cookies['info']
letters = [first]
while next:
    val = next.group(1)
    print(val)
    response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + val)
    print(response.cookies)
    letter = response.cookies['info']
    letters.append(letter)
    next = re.search(r"(\d{2,})", response.text)


print(''.join(letters))
# letters = "BZh91AY%26SY%94%3A%E2I%21%19%80P%81%11%AFg%9E%A0+hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
# letters = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"

as_bytes = (urllib.parse.unquote_to_bytes(''.join(letters).replace("+", " ")))
print(bz2.decompress(as_bytes))


# Solution
# Followed the cookie thing around. Checked cookies (one set by linkedlist.php) says you should have followed busynothing
# So I think that means we change the parameter to ?busynothing=12345
# http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345
# The cookies had letters that when joined started wtih BZh9 => bz2
# Getting binary string and then unzipping =>
# b'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'


#!/usr/bin/env python -w

import xmlrpc.client

with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    print(proxy.system.listMethods())
    print(proxy.system.methodHelp('phone'))
    print(proxy.phone('Leopold'))
    # print("3 is even: %s" % str(proxy.is_even(3)))
    # print("100 is even: %s" % str(proxy.is_even(100)))http://www.pythonchallenge.com/pc/phonebook.php

# solution: calling it with 'Leopold' gave '555-VIOLIN'

# http://www.pythonchallenge.com/pc/stuff/violin.php