# ex22qbDataTextFile
###############################################################################
#
# In-class activity; 12 Mar. 2019
#
###############################################################################


qbfile = open("qbdata.txt", "r")

# print(qbfile.readline())
# print(qbfile.readline())
# line = qbfile.readline()
# print(line)
# print(line)

# for i in qbfile:
#     line = qbfile.readline()
#     print(line)

# line = qbfile.readline()
# numlines = 0
# while line:
#     values = line.split()
#     print('QB ', values[0], values [1], 'had a rating of ', values[10])
#     line = qbfile.readline()
#     numlines += 1
# qbfile.close()
# print(f'{numlines} lines printed')

line = qbfile.readline()
numlines = 1
while numlines < 10:
    values = line.split()
    print(f'{numlines}.  {values[1]} {values[6]}')
    line = qbfile.readline()
    numlines += 1
qbfile.close()
print(f'{numlines} lines printed')
