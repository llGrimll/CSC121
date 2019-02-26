###############################################################################
#
# Recreate an image with just turtles (as efficiently as you can)
# Utilize 1 function, a nested for loop and the usual turtle methods
# Incorporate strategies used on other excercises (NEW: use a loop to create
# turtle instances)
#
###############################################################################

import turtle
import random

x = -100
y = -100


def displayTurtle(t):
    global x
    global y
    color_list = ['Red', 'Green', 'Blue', 'Brown', 'Aqua', 'Black',
                  'Aquamarine', 'Cyan', 'Crimson']
    clr = color_list[random.randint(0, 8)]
    t.hideturtle()
    t.penup()
    t.shape("turtle")
    t.speed(0)
    t.color(clr)
    t.goto(x, y)
    t.left(90)
    t.showturtle()


wn = turtle.Screen()

for i in range(6):
    x = -100
    y += 50
    for i in range(6):
        i = turtle.Turtle()
        displayTurtle(i)
        x += 50


wn.exitonclick()
