#!/usr/bin/env python -w

print 2**38

letters = "abcdefghijklmnopqrstuvwxyz"
print letters.find('k')
print letters.find('m')
print letters.find('o')
print letters.find('q')
print letters.find('e')
print letters.find('g')

url = "map"
decodedurl = "ocr"
code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decoded = ""
for letter in code:
    print letter
    if letter in letters:
        decoded += letters[(letters.find(letter) + 2) % len(letters)]
    else:
        decoded += letter


print decoded
 # http://www.pythonchallenge.com/pc/def/ocr.html