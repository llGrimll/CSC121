###############################################################################
# You are given the following information, but you may prefer to do some
# research for yourself.
#
# A leap year occurs on any year evenly divisible by 4,
# but not on a century (divisible by 100) unless it is divisible by 400.
#
# Print...
#  - the years from 1600-2020
# (Leap years will have the string "-Leap" after the year to identify them
# uniquely)
#  - number of total leap years in that period
#
#  Start with a year counter value at 1599 and conditions of <2020 and >=1599.
#  You may use a while loop and a 'not' operator and some type of counter
#  variable.
#
#  To begin, first print out years divisible by four (most are leap years),
#  then try to incorporate the non-century except /400 rule.
###############################################################################

year = 1599
while year >= 1599 and year <= 2020:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year)
                year + 1
            else:
                year += 1
        else:
            print(year)
    year += 1
