#!/usr/bin/env python -w

from PIL import Image
from collections import deque

image = Image.open('white.gif')
(x_max, y_max) = image.size
new = Image.new(image.mode, (x_max * 2, y_max))
pixels = list(image.getdata())
new_pixels = list(pixels)
new.putdata(new_pixels)


# draw = Image.new()

def get_x_direction(x):
    if x < 100: return 'left'
    if x > 100: return 'right'
    return 'stay'


def get_y_direction(y):
    if y < 100: return 'down'
    if y > 100: return 'up'
    return 'stay'


def get_next_x_position(current, direction):
    if direction == 'right': return current + 1
    if direction == 'left': return current - 1
    return current


def get_next_y_position(current, direction):
    if direction == 'up': return current + 1
    if direction == 'down': return current - 1
    return current


print(x_max, y_max)
print("------------------------------")
print(image.n_frames)
x_position = 50
y_position = 100
for frame in range(image.n_frames):
    for x in range(x_max):
        for y in range(y_max):
            px = image.getpixel((x, y))
            if px:
                x_position = get_next_x_position(x_position, get_x_direction(x))
                y_position = get_next_y_position(y_position, get_y_direction(y))

                # New letter
                if get_x_direction(x) == get_y_direction(y) == 'stay':
                    x_position += 50
                    y_position = 100

                print(x_position, y_position, px)
                new.putpixel((x_position, y_position), 16777215)
                # print(x, y, px, get_x_direction(x), get_y_direction(y), px)
    image.seek(frame)
print("------------------------------")

new.show()

# http://www.pythonchallenge.com/pc/hex/bonus.html