#!/usr/bin/env python -w



def next(current):
    input = str(current)
    all = []
    group = []
    last = input[0]
    for char in input:
        print(char, last)
        if char != last:
            print('New seq')
            all.append(group[:])
            group = []
        group.append(char)
        last = char
    all.append(group)
    print(all)

# Say it outline
# a = [1, 11, 21, 1211, 111221]
next(111221)


# solution:
