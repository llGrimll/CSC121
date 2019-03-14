# ex25studentGrades
###############################################################################
#
# Instructions: Using the text file studentgrades.txt (shown in files) write a
# program that calculates the average grade for each student, and print out the
# student’s name along with their average grade. Then write it to a new file
# named studentavg.txt
#
###############################################################################

student_grade_in_file = open("studentgrades.txt", "r")
student_ave = open("studentsave.txt", "w")

line = student_grade_in_file.readline()

with open('studentgrades.txt') as sg:
    for line in sg:
        values = line.split()
        grades = [int(i) for i in values[1:]]
        total = sum(grades)
        count = len(grades)
        student_average = total / count
        s_ave.write(f'{values[0]} recieved an average of {student_average}.\n')
        line = student_grade_in_file.readline()

student_grade_in_file.close()
student_ave.close()
