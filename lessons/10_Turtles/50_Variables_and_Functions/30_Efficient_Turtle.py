import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 



def draw_polygon(sides):
    
    angle = 360/sides
    for i in range(sides):                 # Loop through the number of sides
        tina.forward(100)                              # Move tina forward by the forward distance
        tina.left(angle)              # Turn tina left by the left turn



tina.goto(0,-100)
draw_polygon(4)                        # Draw a square
                        # Move tina to another spot on the screen
tina.goto(0,-200)
draw_polygon(6)  

tina.goto(0,0)
draw_polygon(5)


 
turtle.exitonclick()   