###############################################################################
#
# Create a polygon that rotates seemingly around a center point with 12
# positions like numbers on a clock
#
###############################################################################
import turtle
import random


def draw_polygon(t):
    color_list = ['Red', 'Green', 'Blue', 'Brown', 'Aqua', 'Black',
                  'Aquamarine', 'Cyan', 'Crimson']
    clr = color_list[random.randint(0, 8)]
    length = 50
    sides = 3
    t.down()
    t.begin_fill()
    t.color(clr)
    for i in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()
    t.up()


def radial_symmetry(t):
    go to 
    for i in range():

    t.goto(0, 0)


tim = turtle.Turtle()
