#!/usr/bin/env python -w


# Inside the zip:
# Yes! This is really level 21 in here.
# And yes, After you solve it, you'll be in level 22!
#
# Now for the level:
#
# * We used to play this game when we were kids
# * When I had no idea what to do, I looked backwards.

import subprocess
import zlib
import bz2
from num2words import num2words


def get_file_type(filename):
    try:
        return subprocess.check_output(['file', filename]).decode()
    except:
        print(f'ERR reading file type for {filename}')
        return 'zlib'





def convert_zlib(src, dest):
    with open(src, 'rb') as s:
        with open(dest, 'wb') as d:
            d.write(zlib.decompress(s.read()))


def convert_bzip2(src, dest):
    with open(src, 'rb') as s:
        with open(dest, 'wb') as d:
            d.write(bz2.decompress(s.read()))

def get_filename(number):
    return num2words(number)

def reverse_file(src):
    read = open(src, 'rb')
    data = read.read()
    read.close()

    write = open(src, 'wb')
    write.write(data[::-1])
    write.close()

code = ''
for i in range(1, 734):
    type = get_file_type(f'./21/{get_filename(i)}')
    if ': data' in type:
        code += '\n'
        print(f'Trying to reverse {get_filename(i)}')
        reverse_file(f'./21/{get_filename(i)}')
        type = get_file_type(f'./21/{get_filename(i)}')
    # print(type)
    if 'zlib' in type:
        code += 'z'
        convert_zlib(f'./21/{get_filename(i)}', f'./21/{get_filename(i+1)}')
    elif 'bzip2' in type:
        code += ' '
        convert_bzip2(f'./21/{get_filename(i)}', f'./21/{get_filename(i+1)}')
    else:
        print(type)
        try:
            convert_zlib(f'./21/{get_filename(i)}', f'./21/{get_filename(i+1)}')
            code += 'z'
        except:
            print('Nope')



# gol ruoy ta kools
print("sgol ruoy ta kool"[::-1])
print(code)

# Had to get hint out the whole z vs space for zlib vs bz2 and reverse is new line but this is the string:
# zzzzzz   zzzzzzzzzz   zzzzzz        zzzz        zzzz          zz
# zzzz       zzzzzz       zzzz         zzz         zzz         zzz
# zzz  zzzzz  zzzz  zzzzz  zzz  zzzzzz  zz  zzzzzz  zz  zzzzzzzzzz  zzzzzz
# zz  zzzzzzzzzzz  zzzzzzz  zz  zzzzzz  zz  zzzzzz  zz  zzzzzzzzzz  zzzzzz
# zz  zzzzzzzzzzz  zzzzzzz  zz         zzz         zzz        zzzz
# zz  zzzzzzzzzzz  zzzzzzz  zz        zzzz        zzzz        zzzz        z
# zz  zzzzzzzzzzz  zzzzzzz  zz  zzzzzzzzzz  zzzzzzzzzz  zzzzzzzzzz  zzz  z
# zzz  zzzzz  zzzz  zzzzz  zzz  zzzzzzzzzz  zzzzzzzzzz  zzzzzzzzzz  zzzz  z
# zzzz       zzzzzz       zzzz  zzzzzzzzzz  zzzzzzzzzz         zzz  zzzzz  z
# zzzzzz   zzzzzzzzzz   zzzzzz  zzzzzzzzzz  zzzzzzzzzz          zz  zzzzzz