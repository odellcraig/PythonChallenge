#!/usr/bin/env python -w

from datetime import datetime
import calendar


# What we know:
# Year is somewhere in the 1000s
# Day of week for Jan 26 is Monday (Jan 26 is a Tues)
# Jan 26 and Jan 27 are important
# Feb has 29 days so its a leap year


def is_leap(date):
    if calendar.isleap(date.year):
        return True
    return False


for year in range(1000, 2000):
    date = datetime(year, 1, 26, 12, 00, 00, 00000)
    if str(date.year)[-1] == '6' and is_leap(date) and date.weekday() == 0:
        print(date)


# 1176-01-01 12:00:00
# 1356-01-01 12:00:00
# 1576-01-01 12:00:00
# 1756-01-01 12:00:00
# 1976-01-01 12:00:00

# 1976 is "youngest" so it must be 1756
# https://www.onthisday.com/people/mozart (from whom?)
# http://www.pythonchallenge.com/pc/return/mozart.html
