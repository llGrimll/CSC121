# You will not do any coding here!

# You will create a new repl (not a file in here) using Python (with Turtle)
# named mt5_lastname (using your last name). mt5 will be shared separately
# from your first repl (this one) with your first 4 activities.

# You will create 5 squares (black outline only) that start with size 50 and
# grow 25% larger each time. They can all start at the same place
# (for simplicity). You should use one function with a for loop and nested
# for loop (that draws the first square), size variable should be local
# (in the function def), and then incremented in the function.
# Use one function call to run it.

# You can copy the comment above to your new repl if you like or even put it in
# a separate file within your repl so it is out of your way.

import turtle


def drawMultipleSquares(t):
    t.speed(5)
    length = 50
    for i in range(5):
        t.penup()
        t.forward(length / 2)
        t.left(90)
        t.pendown()
        t.st()
        for i in range(4):
            t.forward(length / 2)
            t.left(90)
            t.forward(length / 2)
        t.penup()
        t.ht()
        t.goto(0, 0)
        length = length * 1.25


wn = turtle.Screen()
geo = turtle.Turtle()

drawMultipleSquares(geo)

wn.exitonclick()
