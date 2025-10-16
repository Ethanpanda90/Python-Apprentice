import turtle
turtle.setup(600,600,0,0)

def set_turtle_image(turtle,image):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

set_turtle_image(t, 'pikachu.gif')

t.penup()
t.speed(3)

for i in range(4):
    t.goto(200, 200)
    t.goto(-200, -200)

turtle.exitonclick() 