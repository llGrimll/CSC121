# ex6TestScoreLetterGrade

##############################################################################
#
# Create a program that accepts input for test grades and then outputs a
# percentage and then outputs an average.
# Using Code from ex3GradeTestScoreAverage, utilize if elif else conditional
# statements to create print statement that indicates letter grade of average
# average score.
#
##############################################################################

# instructions to make while loop work
print('Enter your test scores below. Once done, hit enter.')

# while loop to end when hitting enter, "''"
count = 0
total_score = 0
test_score = '0'
while (test_score != ''):
    test_score = input('What was your test score: ')
    if test_score == '':
        break
    else:
        total_score += float(test_score)
        count += 1

average = total_score / count
if average > 90:
    if count == 1:
        print(f'Your total grade was a {round(average, 2)} which is an "A" out of 1 test.')
    else:
        print(f'Your total grade was a {round(average, 2)} which is an "A" out of {count} tests.')
elif average > 80:
    if count == 1:
        print(f'Your total grade was a {round(average, 2)} which is an "B" out of 1 test.')
    else:
        print(f'Your total grade was a {round(average, 2)} which is an "B" out of {count} tests.')
elif average > 70:
    if count == 1:
        print(f'Your total grade was a {round(average, 2)} which is an "C" out of 1 test.')
    else:
        print(f'Your total grade was a {round(average, 2)} which is an "C" out of {count} tests.')
elif average > 60:
    if count == 1:
        print(f'Your total grade was a {round(average, 2)} which is an "D" out of 1 test.')
    else:
        print(f'Your total grade was a {round(average, 2)} which is an "D" out of {count} tests.')
else:
    if count == 1:
        print(f'Your total grade was a {round(average, 2)} which is an "F" out of 1 test. Study harder next time!')
    else:
        print(f'Your total grade was a {round(average, 2)} which is an "F" out of {count} tests. Study harder next time!')
