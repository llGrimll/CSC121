import turtle
import random


# one polygon function
def drawPolygon(t):
    # your code here.
    color_list = ['Red', 'Green', 'Blue', 'Brown', 'Aqua', 'Black',
                  'Aquamarine', 'Cyan', 'Crimson']
    clr = color_list[random.randint(0, 8)]
    sides = random.randint(3, 10)
    length = random.randint(10, 60)
    t.pendown()
    t.speed(10)
    t.begin_fill()
    t.color(clr)
    for i in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()
    t.penup()


def drawRowPolygons(t):
    # polygon rows funtion
    for i in range(random.randint(10, 25)):
        x = random.uniform(-200, 200)
        y = random.uniform(-200, 200)
        # number of polygon function
        for i in range(1):
            t.penup()
            t.goto(x, y)
            drawPolygon(geo)


wn = turtle.Screen()
geo = turtle.Turtle()

drawRowPolygons(geo)  # draw a decagon

wn.exitonclick()
