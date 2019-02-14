###############################################################################
#
# Class activites on February 14th, 2019
#
###############################################################################

fruit = ["banana", "oranges", "apples", "kiwis", "grapefruit", "strawberries",
         "peaches"]

# simple for loop
for i in fruit:
    print(i)

# print even indexes
for i in fruit:
    if fruit.index(i) % 2 == 0:
        print(i)

# print odd indexes
for i in fruit:
    if fruit.index(i) % 2 != 0:
        print(i)
