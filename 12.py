#!/usr/bin/env python -w

import io
from PIL import Image


# image = Image.open('evil2.jpg')
# print(image.mode)
# print(image)
# print(image.size)
# (x_max, y_max) = image.size

# rotated = Image.new(image.mode, (x_max, y_max))
pixels = [[], [], [], [], []]

with open('evil2.gfx', 'rb') as gfx:
    bytes = gfx.read()
    for i, byte in enumerate(bytes):
        pixels[i % 5].append(byte)

for pixes in pixels:
    try:
        image = Image.open(io.BytesIO(bytearray(pixes)))
        image.show()
        print(bytearray(pixes[:50]))
    except:
        print('Error')
# Tried to rotate the image in pixels and extract out rpg, then saw it was evil1.jgp
# evil2.jpg evil2.gfx evil3.jpg evil4.jpg (Says Bert is Evil)
# http://www.pythonchallenge.com/pc/return/bert.html says bert is evil
# disproportional  (had to pair together to get this)
