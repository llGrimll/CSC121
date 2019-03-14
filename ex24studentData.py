# ex24studentData
###############################################################################
#
# Instructions: Using the text file studentdata.txt write a program that prints
# out the names of students that have more than six quiz scores.
#
###############################################################################

studentfile = open("studentdata.txt", "r")

line = studentfile.readline()

while line:
    values = line.split()
    if len(values[1:]) >= 6:
        print(f'{values[0]} took {len(values[1:])} quizes.')
    line = studentfile.readline()

studentfile.close()
