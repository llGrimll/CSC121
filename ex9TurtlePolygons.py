import turtle
import random

sides = random.randint(3, 12)  # input('How many sides would you like to see: )
angle = 360 / int(sides)
length = 50
colorlist = ['Red', 'Green', 'Blue', 'Brown', 'Aqua', 'Black', 'Aquamarine',
             'Cyan', 'Crimson']

toby = turtle.Turtle()
toby.shape("turtle")
toby.color(colorlist[random.randint(0, 8)])
toby.speed(3)

toby.begin_fill()
for i in range(int(sides)):
    toby.forward(length)
    toby.left(angle)
toby.end_fill()

toby.penup()
toby.goto(25, -25)
toby.left(90)
