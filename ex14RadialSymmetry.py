###############################################################################
#
# Create a polygon that rotates seemingly around a center point with 12
# positions like numbers on a clock
#
###############################################################################
import turtle
import random

objects = 6
sides = random.randint(3, 5)


def draw_polygon(t):
    color_list = ['Red', 'Green', 'Blue', 'Brown', 'Aqua', 'Black',
                  'Aquamarine', 'Cyan', 'Crimson']
    clr = color_list[random.randint(0, 8)]
    global sides
    length = 40
    t.speed(0)
    t.down()
    t.begin_fill()
    t.color(clr)
    for i in range(sides):
        t.forward(length / 2)
        t.left(360 / sides)
        t.forward(length / 2)
    t.end_fill()
    t.up()


def radial_symmetry(t):
    global objects
    global sides
    draw_polygon(tim)
    angle = 360 / objects
    # making sure the turtle goes to the center depending on the sides
    # the number of sides creates a different sized polygon
    if sides == 3:
        y = 16
    elif sides == 4:
        y = 20
    else:
        y = 25
    t.goto(0, y)
    for i in range(objects):
        t.forward(150)
        t.right(90)
        draw_polygon(tim)
        t.goto(0, y)
        t.left(90 + angle)
    t.hideturtle()


wn = turtle.Screen()
tim = turtle.Turtle()

radial_symmetry(tim)

wn.exitonclick()
