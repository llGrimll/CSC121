###############################################################################
#
# Recreate an image with turtles (as efficiently as you can)
# Utilize muliple functions, function calls, for loops and the usual turtle
# method
# Incorporate stategies used on other exercises
#
###############################################################################

import turtle


# function for the black squares with space in between
def drawSquaresRight(t):
    length = 50
    t.begin_fill()
    # for loop to make one square
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.forward(length * 2)  # skipping the white space creating the white box


# similar fuction as drawSquaresRight, changes black and white space
def drawSecondRow(t):
    length = 50
    t.speed(0)
    t.forward(50)
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.forward(length * 2)  # skipping the white space creating the white box


# function to draw border
def borderFunction(t):
    # go to top left corner
    t.goto(-200, 200)
    t.pendown()
    # faces turtle down
    t.left(180)
    # draws square around the edge
    for i in range(4):
        t.left(90)
        t.forward(400)
    t.hideturtle()


# putting all functions together, creating all rows and border around
def drawCheckerboard(t):
    t.speed(0)
    y = -200
    # number of rows in function
    for i in range(4):
        x = -200
        # creates black squares in odd rows and moves it up to next odd row
        for i in range(4):
            t.penup()
            t.goto(x, y)
            drawSquaresRight(geo)
            x += 100
        y += 100
    y = -150
    # creates black squares in even rows and moves it up to next even row
    for i in range(4):
        x = -200
        for i in range(4):
            t.goto(x, y)
            drawSecondRow(geo)
            x += 100
        y += 100
    borderFunction(geo)


wn = turtle.Screen()
geo = turtle.Turtle()

# calls function
drawCheckerboard(geo)

wn.exitonclick()
