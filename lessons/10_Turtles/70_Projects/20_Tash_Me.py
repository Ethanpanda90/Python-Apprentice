""" 
Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustache
3) Move the moustache to the right spot on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

set_turtle_image(t.'moustache3.gif')

turtle.exitonclick() 