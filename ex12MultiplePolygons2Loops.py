import turtle
import random


def drawPolygon(t, length, sides):
    # your code here.
    color_list = ['Red', 'Green', 'Blue', 'Brown', 'Aqua', 'Black',
                  'Aquamarine', 'Cyan', 'Crimson']
    clr = color_list[random.randint(0, 8)]
    t.pendown()
    t.begin_fill()
    t.color(clr)
    for i in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()
    t.penup()


def drawRowPolygons(t):
    y = 130
    # number of rows function
    for i in range(3):
        x = -130
        # number of polygon in each row function
        for i in range(3):
            t.penup()
            t.goto(x, y)
            drawPolygon(geo, 30, 10)
            x += 130
        y -= 130


wn = turtle.Screen()
geo = turtle.Turtle()

drawRowPolygons(geo)  # draw a decagon

wn.exitonclick()
