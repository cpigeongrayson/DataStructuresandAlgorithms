import turtle

#Create a Turtle screen
screen = turtle.Screen()

# Create a Turtle object
pen = turtle.Turtle()

#Set the speed of the turtle
pen.speed(2)

#Define Colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

#Draw a colorful heptagon
for color in colors:
    pen.color(color)
    pen.forward(100)
    pen.circle(50)
    pen.left(51.5)

#Close the Turtle graphics window on click
screen.exitonclick()

