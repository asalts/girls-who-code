from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:
color = input("enter a color: ")
pencolor(color)

sides = int(input("enter a number of sides: "))
n = 360/sides
for i in range(sides):
    forward(100)
    right(n)

# Close window on click.
exitonclick()
