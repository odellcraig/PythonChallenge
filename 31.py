#!/usr/bin/env python -w
# Start
# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html // continuing password: repeat/switch


from PIL import Image

# Click on image -> kohsamui/thailand
# http://www.pythonchallenge.com/pc/rock/grandpa.html

img = Image.open("mandelbrot.gif")

left = 0.34
bottom = 0.57
width = 0.036
height = 0.027
max = 128

w, h = img.size

xstep = width / w
ystep = height/ h

result = []

for y in range(h - 1, -1, -1):
    for x in range(w):
        c = complex(left + x * xstep, bottom + y * ystep)
        z = 0 + 0j
        for i in range(max):
            z = z * z + c
            if abs(z) > 2:
                break
        result.append(i)

img2 = img.copy()
img2.putdata(result)
img2.show()

diff = [(a - b) for a, b in zip(img.getdata(), img2.getdata()) if a != b]
print(len(diff))

plot = Image.new('L', (23, 73))
plot.putdata([(i < 16) and 255 or 0 for i in diff])
plot.resize((230,730)).show()

# Solution:
# http://www.pythonchallenge.com/pc/rock/arecibo.html

#Notes on text one (don't forget password)
# Looks like warmup.txt is a map for the table columns that we need to setup such that the squares show some shape or clue
