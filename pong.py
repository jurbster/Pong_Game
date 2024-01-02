# Simple Pong game

import turtle

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("light blue")
ball.penup()
ball.goto(0, 0)

# Move paddles
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

window.listen()
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")

# Main game loop
while True:
    window.update()