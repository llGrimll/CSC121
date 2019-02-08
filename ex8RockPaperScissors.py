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

while count < 3:
    user_guess = input('Pick Rock, Paper or Scissors: ')
    user_guess = user_guess.lower()

    # 1 == rock
    if user_guess == 'rock':
        user_selection = 1
    # 2 == paper
    elif user_guess == 'paper':
        user_selection = 2
    # 3 == scissors
    else:
        user_selection = 3

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
        print(f'The computer also chose {user_guess}. You tied!')
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
        user_win += 1
        count += 1
        if user_selection == 1:
            print('You win, Rock crushes scissors!')
        elif user_selection == 2:
            print('You win! Paper covers rock!')
        else:
            print('You win! Scissors cuts paper!')

    print(f'The score is: User - {user_win}, Comp - {comp_win}.')

    if user_win == 2:
        break
    elif comp_win == 2:
        break
    else:
        continue

if user_win == 2:
    print(f"You beat the computer! You won 2 out of a best of 3 games!")
elif comp_win == 2:
    print(f"The computer beat you! You lost 2 out of a best of 3 games!")
