"""
Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help
"""

import random
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(1)                           # Make the turtle move as fast, but not too fast. 

forwards = [ 10, -2, 30, -4, 50, -6 ]
lefts = [ -10, 2, -30, 4, -50, 6 ]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for  i in range(100):

    random_number = random.randint(0, 5)
    forward = forwards[random_number]
    left = lefts[random_number]
    color = colors[random_number]

    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()  