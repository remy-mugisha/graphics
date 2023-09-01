import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.title("Designed by Group4")
screen.bgcolor("white")  # Set background color

# Set up the Turtle
pen = turtle.Turtle()
pen.speed(10)  # Set drawing speed (1 is slow)
pen.penup()

# Set up the rectangular box
box_width = 400
box_height = 200
box_color = "green"

# Draw the rectangular box
pen.goto(-box_width / 2, -box_height / 2)
pen.color(box_color)
pen.begin_fill()
for _ in range(2):
    pen.forward(box_width)
    pen.left(90)
    pen.forward(box_height)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(0, box_height / 2 + 20)  # Position above the box
pen.color("black")  # Set text color
pen.write(" ", align="center", font=("Arial", 14, "bold"))

# List of circle data: (x, y, radius, color, text)
circle_data = [(-100, 0, 40, "red", "CST"),
               (0, 0, 40, "blue", "SoICT"),
               (100, 0, 40, "orange", "CS")]

# Draw the circles using a loop
for x, y, radius, color, text in circle_data:
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

    pen.penup()
    pen.goto(x, y)
    pen.color("white")
    pen.write(text, align="center", font=("Arial", 14, "bold"))

# Hide the Turtle
pen.hideturtle()

# Display the result
screen.mainloop()
