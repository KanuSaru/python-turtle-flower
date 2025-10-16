import turtle # This is what I did this for :p
import time # For the sleep function
import random

# Setup
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
turtle.bgcolor("black")
color = (255, 255, 255)

# Function
def zero_out_turtle():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(0)
    
def flower(repetitions, angle):
    t.pencolor(color)
    for i in range(repetitions):
        t.fd(i)
        t.left(90)
        t.fd(i / 2)
        t.right(angle)
        
# The magic
for i in range(3, 20):
    flower(200, i * 10)
    time.sleep(1)
    zero_out_turtle()

turtle.done()
turtle.exitonclick()