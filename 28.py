#!/usr/bin/env python -w
from PIL import Image
from collections import Counter



img = Image.open('bell.png')
img = img.convert('RGB')
pixels = list(img.getdata())
print(pixels)

greens = []
for p in pixels:
    green = p[1]
    greens.append(green)

diff = [abs(a - b) for a, b in zip(greens[0::2], greens[1::2])]
counts = Counter(diff)
print(diff)
print(counts)
print(len(diff))
not42 = list(filter(lambda x: x != 42, diff))
print(len(not42))


# http://www.pythonchallenge.com/pc/ring/guido.html