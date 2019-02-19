import turtle
import random


def drawPolygon(t, length, sides):
    # your code here.
    t.begin_fill()
    t.color(clr)
    for i in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()
    t.hideturtle()


wn = turtle.Screen()
geo = turtle.Turtle()
color_list = ['Red', 'Green', 'Blue', 'Brown', 'Aqua', 'Black', 'Aquamarine',
              'Cyan', 'Crimson']
clr = color_list[random.randint(0, 8)]

drawPolygon(geo, 30, 10)  # draw a decagon

wn.exitonclick()
