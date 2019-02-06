# ex7RandomNumGenerator

##############################################################################
#
# Create a program that allows input to guess a random number between 1 and 10
# (including 10). It will count your guesses (and print them) and will print a
# statement based on how many guesses it took to guess the numberself.
# You will need to import the random module and use the randint() function.
#
##############################################################################

import random

print('A random number will be chosen between 1 and 10. Lets see how long it\n
      takes to guess the number!')

int_count = 0
rand_num = random.randint(1, 10)

while rand_num > 0:
    number = int(input('Pick a number between 1 and 10: '))
    if number != rand_num:
        int_count += 1
        print(f'That is incorrect. This was turn number {int_count}.')
    else:
        int_count += 1
        print(f'You got the number, {number}.')
        break

if int_count == 1:
    print(f'Wow, you picked the number in 1 attempt! That was a good guess!')
else:
    print(f'You picked the number in {int_count} attempts!')
