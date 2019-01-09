#!/usr/bin/env python -w
from PIL import Image
import array

image = Image.open('maze.png')
(w, h) = image.size

print(w, h)
start = None
stop = None

for x in range(w):
    if image.getpixel((x, 0)) == (0, 0, 0, 255):
        start = (x, 0)
for x in range(w):
    if image.getpixel((x, h - 1)) == (0, 0, 0, 255):
        stop = (x, h - 1)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
white = (255, 255, 255, 255)
next_map = {}
queue = [stop]

while queue:
    pos = queue.pop(0)
    if pos == start:
        break
    for d in directions:
        tmp = (pos[0] + d[0], pos[1] + d[1])
        if not tmp in next_map and 0 <= tmp[0] < w and 0 <= tmp[1] < h and image.getpixel(tmp) != white:
            next_map[tmp] = pos
            queue.append(tmp)

pos = start
data = []
while pos != stop:
    pixel = image.getpixel(next_map[pos])
    print(next_map[pos], pixel)
    byte = pixel[0]
    data.append(byte)
    pos = next_map[pos]

print(data)
print(data[::2])
print(array.array('B', data[::2]).tostring())
open('maze.zip', 'wb').write(bytes(data[::2]))  # Every other one is a byte
print(start, stop)

# Basically bread first search and then use the path to extract the data
# http://www.pythonchallenge.com/pc/hex/lake.html
