#!/usr/bin/env python -w
# Pickle was the hint
# Pickle is a python library like zip
import pickle

file = open('banner.p', 'rb')
decoded = pickle.load(file)
print decoded[0][0]
for keys in decoded:
    word = ""
    for char in keys:
        word += "".join(([char[0]]*char[1]))
    print word
file.close()


# solution:
#  channel