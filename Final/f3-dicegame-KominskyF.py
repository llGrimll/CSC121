# Create a dice game between Bill & Ted.
# When the game starts Bill will display 3 numbers (2 die and a total), and so
# will Ted. Higher total wins.
# The max/min of the 2 die is 1, 6 (like a normal dice)
# The game will play 2 out of 3, declaring the winner after 2 wins; ties do not
# count.
# Create 2 functions called rolldice() and startgame().
# startgame() will take input r to start the game and call the rolldice()
# function.
# Note: Import random module. You may need to use the global keywoard for
# points if declared outside the function (starting at 0) and modified
# (adding points) inside a function.

import random

bp = 0
tp = 0


def check_win():
    global bp
    global tp
    if bp == 2:
        print(f"Bill won the best of 3!")
        quit()
    elif tp == 2:
        print(f"Ted won the best of 3!")
        quit()
    else:
        print(f'The score is: Bill - {bp}, Ted - {tp}.')
        start_game()


def start_game():
    start_game = input("Type 'r' to Roll Dice: ")
    if start_game != 'r':
        print("Please input 'r' to begin")
        start_game()
    dicegame()


def dicegame():
    global tp
    global bp
    b_roll1 = random.randint(1, 6)
    b_roll2 = random.randint(1, 6)
    t_roll1 = random.randint(1, 6)
    t_roll2 = random.randint(1, 6)
    b_total = b_roll1 + b_roll2
    t_total = t_roll1 + t_roll2
    print(f'Bill   {b_roll1}, {b_roll2}      Total: {b_total}')
    print(f'Ted   {t_roll1}, {t_roll2}      Total: {t_total}')
    if b_total > t_total:
        bp += 1
        check_win()
    elif t_total > b_total:
        tp += 1
        check_win()
    else:
        print("Tied!")
        start_game()


start_game()
