import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Designed by Group4")

# Create a turtle instance
pen = turtle.Turtle()

# Draw the blue rectangle
pen.penup()
pen.goto(-150, -50)
pen.pendown()
pen.color("blue")
pen.begin_fill()
for _ in range(2):
    pen.forward(300)
    pen.left(90)
    pen.forward(120)
    pen.left(90)
pen.end_fill()

# Write "Welcome to UR " in the rectangle
pen.penup()
pen.goto(0 ,0)
pen.color("white")
pen.write("Welcome to UR CST", align="center", font=("Arial", 12, "bold"))

# Hide the turtle
pen.hideturtle()

# Keep the window open until it's manually closed
turtle.done()