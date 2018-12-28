#!/usr/bin/env python -w
# Pickle was the hint
# Pickle is a python library like zip

import re
import zipfile


def file_get_contents(filename):
    with open(filename) as f:
        return f.read()


archive = zipfile.ZipFile(r'channel.zip', 'r')
comments = ""
next = re.search(r"(\d+)", 'Start with 90052')
while next:
    val = next.group(1)
    comment = archive.getinfo(f'{val}.txt').comment
    comments += str(comment.decode("utf-8") )
    contents = file_get_contents(f'channel/{val}.txt')
    print (f'{val} -> {contents}')
    next = re.search(r"(\d+)", contents)

print (comments)

# solution:
#  change channel.html to channel.zip it will download a zip which has a linked list of files
#  followed linked list and got the phrase "Collect the Comments"... turns out zip files can have comments... so had to use python to read them
# using comments and converting to chars gave this:
# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
# **************************************************************

# Turns out the answer is actually the letters and its 'oxygen'


