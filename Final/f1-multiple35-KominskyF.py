###############################################################################
# If we list all the natural numbers from 1 to 10 that are multiples of 3 or 5,
# we would return 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Print out...
# - All the multiples of 3 or 5 from 1-500.
# - The total number of multiples of 3 or 5
# - The sum of the the multiples
#
# Call a function to do this. You will need a counter, a loop and conditions,
# as well as 3 print statements.
# NOTE: To determine a multiple, use a modulus (x%3==0, multiple of 3) to
# deretmine a multiple of an integer
###############################################################################


def multiples():
    x = 1
    multiples = []
    for i in range(500):
        if x % 3 == 0 or x % 5 == 0:
            multiples.append(x)
        x += 1
    print(multiples)
    print(len(multiples))
    print(sum(multiples))


multiples()
