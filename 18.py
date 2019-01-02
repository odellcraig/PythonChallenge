#!/usr/bin/env python -w

import io
from PIL import Image
import difflib

# image = Image.open('balloons.jpg')
# (x_max, y_max) = image.size
# half = int(x_max / 2)
# one = Image.new(image.mode, (half, y_max))
# two = Image.new(image.mode, (half, y_max))
# pixels = list(image.getdata())
#
# print(x_max, y_max)
#
# one_pixels = []
# two_pixels = []
# for row in range(y_max):
#     start = row * x_max
#     one_pixels.extend(pixels[start: start + half])
#     two_pixels.extend(pixels[start + half: start + x_max])
#
# print(len(one_pixels))
# print(len(two_pixels))
# one.putdata(one_pixels)
# two.putdata(two_pixels)
#
# one.show()
# two.show()

dleft = []
dright = []
with open('deltas', 'r') as deltas:
    for line in deltas:
        dleft.append(line[:53] + '\n')
        dright.append(line[56:])

print(dleft)
print('----------------')
print(dright)
print('----------------')
left = []
right = []
same = []
for line in difflib.Differ().compare(dleft, dright):
    if line[0] == '-':
        for b in line[1:].split():
            left.append(int(b, 16))
    elif line[0] == '+':
        for b in line[1:].split():
            right.append(int(b, 16))
    else:
        for b in line[1:].split():
            same.append(int(b, 16))

print(left)
print(right)
print(same)

left = Image.open(io.BytesIO(bytearray(left)))
left.show()

right = Image.open(io.BytesIO(bytearray(right)))
right.show()

same = Image.open(io.BytesIO(bytearray(same)))
same.show()

# solution:
# tried to diff the pixels, but didn't see anything so got a hint and tried brightness.html
# brightness.html view source gave me deltas.gz
# deltas looked like two images, but turns out it was something we had to dif
# So really three images (+ of diff - of diff and same of diff)
# images show "fly" "butter" and "../hex/bin.html"
# http://www.pythonchallenge.com/pc/hex/bin.html
# uname: butter
# password: fly