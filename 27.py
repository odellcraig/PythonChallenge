#!/usr/bin/env python -w
from PIL import Image
import codecs
import bz2

def hex(s): return codecs.getencoder('hex')(s)[0]

image = Image.open('zigzag.gif')
(w, h) = image.size

palette = image.getpalette()[::3]
b = bytes([i for i in range(256)])
print(len(bytes(palette)))
print(b)

translator = bytes.maketrans(b, bytes(palette))
print(translator)

raw = image.tobytes()
trans = raw.translate(translator)
zipped = list(zip(raw[1:], trans[:-1]))

print(zipped)
diff = list(filter(lambda p: p[0] != p[1], zipped))
indices = [i for i,p in enumerate(zipped) if p[0] != p[1]]

print(diff)
print(indices)

im2 = Image.new("RGB", image.size)
colors = [(255, 255, 255)] * len(raw)
for i in indices:
    colors[i] = (0, 0, 0)
im2.putdata(colors)
im2.show()


s = [t[0] for t in diff]
text = bz2.decompress(bytes(s))

import keyword
print(set([w for w in text.split() if not keyword.iskeyword(w.decode())]))
# Well, this level needs to be updated, since exec and print are not keywords in Python 3. The only two words left are repeat and switch
# username: repeat
# password: switch
# This one was obscure and I needed help a lot