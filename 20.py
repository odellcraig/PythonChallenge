#!/usr/bin/env python -w

import requests
import shutil
import re


# next = re.search(r"\d+-(\d+)/(\d+)", '0-2123456789/2123456789')
# while next:
#     val = next.group(1)
#     print(val)
#     headers = {'Range': f'bytes={int(val)+1}-'}
#     # headers = {'Range': f'bytes=30203-'}
#     response = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers=headers, auth=('butter', 'fly'), stream=True)
#     print(response.text)
#     print(response.headers)
#     print(response.headers['content-range'])
#     next = re.search(r"bytes \d+-(\d+)\/(\d+)", response.headers['content-range'])

# solution: had to do content-range (range) for each chunk then you guess by doing it after the lenght and you get
# esrever ni emankcin wen ruoy si drowssap eht

result = 'esrever ni emankcin wen ruoy si drowssap eht'
print(result[::-1])
print('invader'[::-1])
print('idiot'[::-1])

# Now reverse the search:

# next = re.search(r"\d+-(\d+)/(\d+)", '0-2123456742/2123456789')
# while next:
#     val = next.group(1)
#     print(val)
#     headers = {'Range': f'bytes={int(val)+1}-'}
#     # headers = {'Range': f'bytes=30203-'}
#     response = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers=headers, auth=('butter', 'fly'), stream=True)
#     print(response.text)
#     print(response.headers)
#     print(response.headers['content-range'])
#     next = re.search(r"(\d+)", response.text)

# and its hiding at 1152983631

headers = {'Range': f'bytes=1152983631-'}
response = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers=headers, auth=('butter', 'fly'), stream=True)
with open('20.zip', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

# 20.zip is the result password protected with "redavni"

# Inside the zip:
# Yes! This is really level 21 in here.
# And yes, After you solve it, you'll be in level 22!
#
# Now for the level:
#
# * We used to play this game when we were kids
# * When I had no idea what to do, I looked backwards.

