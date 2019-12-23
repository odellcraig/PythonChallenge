#!/usr/bin/env python -w

import re
import bz2

b = []
number = 1
with open('silence.htm') as html:
    for line in html:
        number += 1
        if not re.search(r'\S+', line):
            b.append(len(line))

print(bytes(b))
print(bytes(b).hex())
#
# text = bz2.decompress(bytes(b))
# print(text)

# Had it right but google must mangle the line endings or something


from urllib.request import Request, urlopen
import bz2, base64

req = Request('http://www.pythonchallenge.com/pc/ring/guido.html')
req.add_header('Authorization', 'Basic %s' % base64.b64encode(b'repeat:switch').decode())
raw = urlopen(req).read().splitlines()[12:]
data = bytes([len(i) for i in raw])
print(data)
print(bz2.decompress(data))


# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html // continuing password: repeat/switch