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

while count != 3:
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

    # user chose rock
    if user_selection == 1:
        if comp_guess == 1:  # comp chooses rock
            print('You tied!')
        elif comp_guess == 2:  # comp chooses paper
            comp_win += 1
            count += 1
            print('You lose, computer chose paper.')
        else:  # comp chooses scissors
            user_win += 1
            count += 1
            print('You win, computer chose scissors.')

    # user chose paper
    if user_selection == 2:
        if comp_guess == 1:  # comp chooses rock
            user_win += 1
            count += 1
            print('You win, computer chose scissors.')
        elif comp_guess == 2:  # comp chooses paper
            print('You tied!')
        else:  # comp chooses scissors
            comp_win += 1
            count += 1
            print('You lose, computer chose paper.')

    # user chose scissors
    if user_selection == 3:
        if comp_guess == 1:  # comp chooses rock
            comp_win += 1
            count += 1
            print('You lose, computer chose paper.')
        elif comp_guess == 2:  # comp chooses paper
            user_win += 1
            count += 1
            print('You win, computer chose scissors.')
        else:  # comp chooses scissors
            print('You tied!')

    print(f'The score is: User - {user_win}, Comp - {comp_win}.')

    if user_win == 2:
        break
    elif comp_win == 2:
        break
    else:
        continue

if user_win == 2:
    print(f"You beat the computer! You won 2 out of 3 games!")
else:
    print(f"The computer beat you! You lost 2 out of 3 games!")
