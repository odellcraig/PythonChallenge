#!/usr/bin/env python -w

from PIL import Image

image = Image.open('evil1.jpg')
print(image)
print(image.size)
(x_max, y_max) = image.size


ired = Image.new(image.mode, (x_max, y_max))
iblue = Image.new(image.mode, (x_max, y_max))
igreen = Image.new(image.mode, (x_max, y_max))
images = [ired, iblue, igreen]

red = []
blue = []
green = []
pixels = [red, blue, green]


for y in range(y_max):
    for x in range(x_max):
        for i in range(3):
            pixel = [0, 0, 0]
            pixel[i] = image.getpixel((x, y))[i]
            pixels[i].append(tuple(pixel))

for i in range(3):
    images[i].putdata(pixels[i])
    images[i].show()
# solution: evil
# http://www.pythonchallenge.com/pc/return/evil.html
