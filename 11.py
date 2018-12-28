#!/usr/bin/env python -w

from PIL import Image

image = Image.open('cave.jpg')
print(image)
print(image.size)
(x_max, y_max) = image.size

odd_image = Image.new(image.mode, (int(x_max / 2), int(y_max / 2)))
even_image = Image.new(image.mode, (int(x_max / 2), int(y_max / 2)))

odd = []
even = []
for y in range(y_max):
    for x in range(x_max):
        if not (x % 2) and not (y % 2):
            even.append(image.getpixel((x, y)))
        else:
            odd.append(image.getpixel((x, y)))

print(len(even))
print(len(odd))
even_image.putdata(even)
even_image.show()

# solution: evil
# http://www.pythonchallenge.com/pc/return/evil.html