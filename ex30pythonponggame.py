# Simple pong for Beginners
# ex30 CSC121

import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Kominsky")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .25
ball.dy = .25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Please A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()  # updates window everytime this loops

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    # Top and Bottom Check
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
        #  winsound.PlaySound("C:/Users/jkom8/Dropbox (Personal)/Personal/github/CSC121/ex30ponggamepython/bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        #  winsound.PlaySound("C:/Users/jkom8/Dropbox (Personal)/Personal/github/CSC121/ex30ponggamepython/bounce.wav", winsound.SND_ASYNC)

    # Left and Right Check
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Please A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Please A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Bounce off paddle
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < (paddle_b.ycor() + 40)) and (ball.ycor() > (paddle_b.ycor() - 40)):
        ball.setx(330)
        ball.dx *= -1
        ball.dx += .01
        ball.dy += .01
        #  winsound.PlaySound("C:/Users/jkom8/Dropbox (Personal)/Personal/github/CSC121/ex30ponggamepython/bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < (paddle_a.ycor() + 40)) and (ball.ycor() > (paddle_a.ycor() - 40)):
        ball.setx(-330)
        ball.dx *= -1
        ball.dx += .01
        ball.dy += .01
        #  winsound.PlaySound("C:/Users/jkom8/Dropbox (Personal)/Personal/github/CSC121/ex30ponggamepython/bounce.wav", winsound.SND_ASYNC)
