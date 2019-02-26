###############################################################################
#
# Recreate an image with turtles (as efficiently as you can)
# Utilize muliple functions, function calls, for loops and the usual turtle
# method
# Incorporate stategies used on other exercises
#
###############################################################################

import turtle
import random


def drawSquaresRight(t):
    length = 50
    t.speed(0)
    # t.pendown()
    t.begin_fill()
    for i in range(4):
        t.color("black")
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.forward(50)
    for i in range(4):
        t.pendown()
        t.forward(length)
        t.left(90)
        t.penup()
    t.forward(length)
    # t.penup()


def drawSecondRow(t):
    length = 50
    t.speed(0)
    # t.pendown()
    for i in range(4):
        t.pendown()
        t.forward(length)
        t.left(90)
        t.penup()
    t.forward(50)
    t.begin_fill()
    for i in range(4):
        t.color("black")
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.forward(length)
    # t.penup()


def borderFunction(t):
    t.goto(-200, 200)
    t.pendown()
    t.left(180)
    for i in range(4):
        t.left(90)
        t.forward(400)
    t.hideturtle()


wn = turtle.Screen()
geo = turtle.Turtle()


def drawRowsSquares(t):
    y = -200
    # number of rows in function
    for i in range(4):
        x = -200
        for i in range(4):
            t.penup()
            t.goto(x, y)
            drawSquaresRight(geo)
            x += 100
        y += 100
    y = -150
    for i in range(4):
        x = -200
        for i in range(4):
            t.penup()
            t.goto(x, y)
            drawSecondRow(geo)
            x += 100
        y += 100
    borderFunction(geo)


drawRowsSquares(geo)
