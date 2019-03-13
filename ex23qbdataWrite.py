# ex23qbDataWrite
###############################################################################
#
# In-class activity; 12 Mar. 2019
#
###############################################################################

qbinfile = open("qbdata.txt", "r")
qboutfile = open("qbyards.txt", "w")

line = qbinfile.readline()
numlines = 1
with open('qbdata.txt') as sg:
    for line in sg:
        values = line.split()
        qboutfile.write(f'{numlines}.  {values[1]} {values[6]}\n')
        line = qbinfile.readline()
        numlines += 1
    numlines -= 1
    qboutfile.write(f'{numlines} lines printed')

qbinfile.close()
qboutfile.close()
