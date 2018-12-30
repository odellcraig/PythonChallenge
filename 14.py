#!/usr/bin/env python -w

from PIL import Image
import numpy as np


def spiral_matrix(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m


image = Image.open('wire.png')
(x_max, y_max) = image.size
unwrapped = Image.new(image.mode, (100, 100))
pixels = list(image.getdata())

for p in pixels[:100]:
    print(p)

print(np.empty([100, 100]))
print(spiral_matrix(100))

pixelspiral = []
spiral = spiral_matrix(100)
for r in spiral:
    for c in r:
        pixelspiral.append(pixels[c-1])
unwrapped.putdata(pixelspiral)
unwrapped.show()
# for i in spiral_matrix(100): print(*i)

# solution: Spiral Matrix was the key. Then generated a spiral matrix and then iterated over the spiral matrix and pulled out the appropriate pixels, then displayed and: cat
# http://www.pythonchallenge.com/pc/return/cat.html
# 
#  -> http://www.pythonchallenge.com/pc/return/uzi.html