#!/usr/bin/env python -w


def next(current):
    str_current = str(current)
    grouped = []
    group = []
    last = str_current[0]
    for char in str_current:
        if char != last:
            grouped.append(group[:])
            group = []
        group.append(char)
        last = char
    grouped.append(group)

    output = ''
    for group in grouped:
        output += f'{len(group)}{group[0]}'
    return output

# sample of sequence
# a = [1, 11, 21, 1211, 111221]

j = 1
for i in range(30):
    j = next(j)
    print(len(j))

# solution: http://www.pythonchallenge.com/pc/return/5808.html
