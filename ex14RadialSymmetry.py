###############################################################################
#
# Create a polygon that rotates seemingly around a center point with 12
# positions like numbers on a clock
#
###############################################################################
import turtle
import random

objects = 12
length = 50


def draw_polygon(t):
    color_list = ['Red', 'Green', 'Blue', 'Brown', 'Aqua', 'Black',
                  'Aquamarine', 'Cyan', 'Crimson']
    clr = color_list[random.randint(0, 8)]
    global length
    sides = random.randint(3, 5)
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
    global length
    global objects
    draw_polygon(tim)
    angle = 360 / objects
    t.goto(0, 20)
    for i in range(objects):
        t.forward(200)
        t.right(90)
        draw_polygon(tim)
        t.goto(0, 20)
        t.left(90 + angle)
    t.hideturtle()


wn = turtle.Screen()
tim = turtle.Turtle()

radial_symmetry(tim)

wn.exitonclick()
