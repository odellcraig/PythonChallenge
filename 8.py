#!/usr/bin/env python -w

import bz2


username = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print (bz2.decompress(username))
print (bz2.decompress(password))



# solution:
# Bee image has a link in it that goes to basic auth, this was in the source:
# un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
# Googling BZh91AY showed bz2 module - I bet you these are bzipped
# Decoding gave 'huge' and 'file' clicking on bee and putting in creds gave good.html
# http://www.pythonchallenge.com/pc/return/good.html

