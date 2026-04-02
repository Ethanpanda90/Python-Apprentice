"""
FizzBuzz Grid

We're going to use a Windowing library, guizero, to create a 10x10 grid of
numbers, with each number in a separate cell, but we're also going to set the
color of the number based on the following rules:

* If the number is evenly divisible by 5, print '🦡'
* If the number is evenly divisible by 3, print '🍄'
* If the number is evenly divisible by 15, print '🐍'
* If it is divisible by neither, print the number.

Additionally, If you are displaying a number  color the numbers as follows:

* If the sum of the digits of the number is even, color the number blue
* If the sum of the digits of the number is odd, color the number red

Here is how you can display a number in your grid. Call this function in your loop
to display the number in the grid cell at the row and column you specify.

    Text(app, text=str(number), grid=[col, row], color=color)

Or to display a badger: 
    
    Text(app, text='🦡', grid=[col, row], color=color)

HINT: You can use % and // to get the first and last digit of a number, 
or you can convert the number to a string and iterate over the digits
"""

from guizero import App, Box, Text

app = App("Numbers Grid", layout="grid", width=333, height=333)

numberthing = 0
for i in range(10):
    for j in range(10):
        numberthing += 1
        if numberthing % 2 == 0:
            oddoreven = 'blue'
        else:
            oddoreven = 'red'
        Text(app, text=str(numberthing), grid=[j, i], color=str(oddoreven))
# Create a 10x10 grid using nested loops
# Or you can use a single loop and calculate the row and column
app2 = App("Numbers Grid", layout="grid", width=333, height=333)
numberthing2 = 0
for i2 in range(10):
    for j2 in range(10):
        numberthing2 += 1
        if numberthing2 % 15 == 0:
            Text(app2, text='🐍', grid=[j2, i2], color='black')
        elif numberthing2 % 5 == 0:
            Text(app2, text='🦡', grid=[j2, i2], color='black')
        elif numberthing2 % 3 == 0:
            Text(app2, text='🍄', grid=[j2, i2], color='black')
        else:
            Text(app2, text=str(numberthing2), grid=[j2, i2], color='black')

# In the loop, calculate or increment the number
for i in range(1,31):

    if i % 15 == 0:
        print(i, '🐍 snake!')
    elif i % 5 == 0:
        print(i, '🦡 badger')
    elif i % 3 == 0:
        print(i, '🍄 mushroom')
    else:
        print(i)
app.display()



# If you are displaying a number, calculate the sum of the digits and determine the color

# Call Text(app, text='...', grid=[col, row], color=...) to display something. 
