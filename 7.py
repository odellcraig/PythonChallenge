#!/usr/bin/env python -w

# solution:
from PIL import Image

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. 0123456789'
ords = list(map(lambda x: ord(x), chars))


def is_ascii(byte):
    return byte >= 32 and byte < 127
    # return byte in ords


converted = ''
with Image.open("oxygen.png") as imageFile:
    pix = imageFile.load()
    (xMax, yMax) = imageFile.size
    for y in range(yMax):
        for x in range(0, xMax, 7): # 7 pixels the same in a row
            (r,g,b,a) = pix[x,y]
            if r == g and g == b and is_ascii(r):
                print (r)
                if (converted == '' or chr(r)):
                    converted += chr(r)

print (converted)

# Solution:
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
# [105, 110, 116, 101, 103, 114, 105, 116, 121] converts to 'integrity'

chars = [105, 110, 116, 101, 103, 114, 105, 116, 121]
decoded = ""
for c in chars:
    decoded += chr(c)
print (decoded)
