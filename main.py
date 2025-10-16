import turtle # This uses the turtle graphics library to draw shapes
import time # For the sleep function
import random

# Setup
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
turtle.bgcolor("black")
color = (random.random(), random.random(), random.random())

# Function
def zero_out_turtle():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(0)
    
# Draw a flower with a given number of repetitions and angle
def flower(repetitions, angle):
    t.pencolor(color)
    for i in range(repetitions):
        t.fd(i)
        t.left(90)
        t.fd(i / 2) 
        t.right(angle)
        
# The magic
for i in range(3, 20):
    flower(300, i * 1) # Change the multiplier to change the angle, so you get different shapes!
    time.sleep(1)
    zero_out_turtle()

turtle.done()