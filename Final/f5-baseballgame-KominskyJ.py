# Depending on your ability with Python: You can either create a baseball game
# based on one at bat where...
# pitches are thrown and they are either strikes or balls. 3 strikes and your
# out or 4 balls is a walk - whichever comes first that's it.
# It should start with an input 'p' to pitch - which initiates the random
# strike or ball.
# Should all take place in a while loop where balls <4 and strikes <3:
# --or slightly extended version--
# Create a version, where in addition to watching pitches - and getting a ball
# or strike (not swinging)  you can choose to swing and either miss (and get a
# strike), get a hit (and end the game) or hit into an out (flyout) and also
# end the game. Choose however simple or complex you'd like it to be.
# See sample output image to see just the (no swing) interaction and output to
# completion (4 balls = walk)

import random

balls = 0
strikes = 0

print("\nBATTER UP!\n")

while balls < 4 and strikes < 3:
    user = input("Type 's' to swing or 'n' to not swing: ")
    if user == 'n':
        pitch = random.randint(1, 100)
        if pitch <= 62:  # 62% MLB average strike percentage
            strikes += 1
            print(f"Strike {strikes}")
        else:
            balls += 1
            print(f"Ball {balls}")
    elif user == 's':
        hit = random.randint(1, 100)
        if hit <= 76:  # 76% contact percentage, info from friend who is a baseball analytics professional
            hit = random.randint(1, 100)
            if hit <= 50:  # 50/50 foul balls/in play
                hit = random.randint(1, 100)
                if hit <= 37:  # Aaron Judge's batting average of balls in play
                    print("You hit the ball and won the game!")
                    quit()
                else:
                    print("You hit the ball but was thrown out. Good luck next at-bat!")
                    quit()
            else:
                if strikes == 2:
                    print("You hit a foul ball with two strikes. Try again.")
                else:
                    print("You hit a foul ball. That's a strike.")
                    strikes += 1
        else:
            print("You swung and missed. That's a strike!")
            strikes += 1
    else:
        print("Please input 's' or'n' to select your action.")
    print(f'Balls: {balls} Strikes: {strikes}')

if balls == 4:
    print("You walked!")
else:
    print("You struck out!")
