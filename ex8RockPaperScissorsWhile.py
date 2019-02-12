# ex8RockPaperScissors
#
###############################################################################
#
# Create a program that allows input of rock, paper or scissors and computer
# output of a random choice or three. We will print results nd keep score,
# allow multiple attempts.
#
# Output will be:
# Computer chose: rock (paper or scissors)
# You either win, lose ot tie each time - ("Rock crushes Scissors", "Scissors
# cuts Paper", or "Paper covers Rock") We will keep score (Best of 3).
#
###############################################################################

import random

count = 0
user_win = 0
comp_win = 0

while count < 5:
    user_guess = input('Pick Rock, Paper or Scissors: ')
    user_guess = user_guess.lower()

    # 1 == rock
    if user_guess == 'r':
        user_selection = 1
    # 2 == paper
    elif user_guess == 'p':
        user_selection = 2
    # 3 == scissors
    elif user_guess == 's':
        user_selection = 3
    else:
        user_selection = 4
        print('Please choose a correct input: [R]ock, [P]aper or [S]cissors.')

    comp_guess = random.randint(1, 3)

    # 1 == rock
    if comp_guess == 1:
        comp_selection = 'rock'
    # 2 == paper
    elif comp_guess == 2:
        comp_selection = 'paper'
    # 3 == scissors
    else:
        comp_selection = 'scissors'

    # user chose rock
    if user_selection == comp_guess:
        print(f'The computer also chose {comp_selection}. You tied! Try again!')
    # user - rock ; comp - paper ; lose
    elif user_selection == 1 and comp_guess == 2:
        comp_win += 1
        count += 1
        print(f'The computer chose {comp_selection}.\nYou lose. Paper covers rock.')
    # user - paper ; comp - scissors ; lose
    elif user_selection == 2 and comp_guess == 3:
        comp_win += 1
        count += 1
        print(f'The computer chose {comp_selection}.\nYou lose! Scissors cuts paper.')
    # user - scissors ; comp - rock ; lose
    elif user_selection == 3 and comp_guess == 1:
        comp_win += 1
        count += 1
        print(f'The computer chose {comp_selection}.\nYou lose! Rock crushes scissors.')
    # all else is a win
    else:
        if user_selection == 4:
            continue
        user_win += 1
        count += 1
        if user_selection == 1:
            print('You win, Rock crushes scissors!')
        elif user_selection == 2:
            print('You win! Paper covers rock!')
        else:
            print('You win! Scissors cuts paper!')

    print(f'The score is: User - {user_win}, Comp - {comp_win}.')

    if user_win == 3:
        break
    elif comp_win == 3:
        break
    else:
        continue

if user_win == 3:
    print(f"You beat the computer! You won 2 out of {count} games!")
elif comp_win == 3:
    print(f"The computer beat you! You lost 2 out of {count} games!")
