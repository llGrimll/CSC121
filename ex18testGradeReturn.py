# ex18testGradeReturn
###############################################################################
#
# In-Class activity - 28 Feb. 2019
#
###############################################################################


def figureAvg(sumt, numt):
    return sumt / numt


tests = []
# while loop to allow infinite input until input is blank
while True:
    testscore = input("Enter your scores: ")
    # break while loop when input is blank
    if testscore == '':
        break
    # changing input to float
    testscore = float(testscore)
    # adds input to list
    tests.append(testscore)


# adds all items in list
sumt = sum(tests)
# amount of items in list
numt = len(tests)

# calculating the average with figureAvg function
avg = figureAvg(sumt, numt)

# print statements depending on grade average
if avg >= 90:
    if numt == 1:
        print(f'''Your total grade was a {round(avg, 2)} which is an "A"\n
              out of 1 test.''')
    else:
        print(f'''Your total grade was a {round(avg, 2)} which is an "A"\n
              out of {numt} tests.''')
elif avg >= 80:
    if numt == 1:
        print(f'''Your total grade was an {round(avg, 2)} which is a "B"\n
              out of 1 test.''')
    else:
        print(f'''Your total grade was an {round(avg, 2)} which is a "B"\n
              out of {numt} tests.''')
elif avg >= 70:
    if numt == 1:
        print(f'''Your total grade was a {round(avg, 2)} which is a "C"\n
              out of 1 test.''')
    else:
        print(f'''Your total grade was a {round(avg, 2)} which is a "C"\n
              out of {numt} tests.''')
elif avg >= 60:
    if numt == 1:
        print(f'''Your total grade was a {round(avg, 2)} which is a "D"\n
              out of 1 test.''')
    else:
        print(f'''Your total grade was a {round(avg, 2)} which is a "D"\n
              out of {numt} tests.''')
else:
    if numt == 1:
        print(f'''Your total grade was a {round(avg, 2)} which is an "F"\n
              out of 1 test. Study harder next time!''')
    else:
        print(f'''Your total grade was a {round(avg, 2)} which is an "F"\n
              out of {numt} tests. Study harder next time!''')
