"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup(600,600,0,0)               # Set the size of the window
window = turtle.Screen()


t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0) 

def make_a_hexagon(t):
    for i in range(3):
        t.pencolor('Black')
        t.forward(100)
        t.left(60)
        t.pencolor(getRandomColor())
        t.forward(100)
        t.left(60)
        
def make_a_circle(t):
    for i in range(360):
        t.pencolor('Black')
        t.forward(60)
        t.left(1)

# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

num_shapes = 67

for i in range(36):
    t.fillcolor('Black')
    t.begin_fill()
    make_a_hexagon(t)
    t.right(360/num_shapes)
    t.end_fill
    t.fillcolor(getRandomColor())
    t.begin_fill()
    make_a_hexagon(t)
    t.right(360/num_shapes)
    t.end_fill()

for i in range(120):
    turtle.fillcolor('Black')
    make_a_circle(t)

turtle.hideturtle()
turtle.done()