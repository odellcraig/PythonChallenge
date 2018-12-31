#!/usr/bin/env python -w

from PIL import Image
from collections import deque

image = Image.open('mozart.gif')
(x_max, y_max) = image.size
aligned = Image.new(image.mode, (x_max, y_max))
pixels = list(image.getdata())


def subfinder(mylist, pattern):
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            return i


pattern = [195]*5
rotated_pixels = []
for row in range(y_max):
    start = row * x_max
    pixel_row = pixels[start : start + x_max]
    pattern_index = subfinder(pixel_row, pattern)
    rotatable = deque(pixel_row)
    rotatable.rotate(x_max - pattern_index)
    print(rotatable)
    rotated_pixels.extend(list(rotatable))


aligned.putdata(rotated_pixels)
aligned.show()

# solution: aligned all the dashes on the row to the beginning of the line and pic showed "romance"
# http://www.pythonchallenge.com/pc/return/romance.html