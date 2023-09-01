import turtle
import math
# Set up the turtle screen
screen = turtle.Screen()
screen.title("Designed by Group 4")  
screen.setup(600, 600)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
turtle.hideturtle()
turtle.speed(0)
turtle.bgcolor('black')
# Define a function to draw a star
def star(x, y, length, penc, fillc):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(90)
    turtle.fd(length)
    turtle.seth(180 + 36 / 2)
    L = length * math.sin(36 * math.pi / 180) / math.sin(54 * math.pi / 180)
    turtle.seth(180 + 72)
    turtle.down()
    turtle.fillcolor(fillc)
    turtle.pencolor(penc)
    turtle.begin_fill()
    for _ in range(5):
        turtle.fd(L)
        turtle.right(72)
        turtle.fd(L)
        turtle.left(144)
    turtle.end_fill()
# Define a recursive function to draw a star fractal
def star_fractal(x, y, length, penc, fillc, n):
    if n == 0:
        star(x, y, length, penc, fillc)
        return
    length2 = length / (1 + (math.sin(18 * math.pi / 180) + 1) / math.sin(54 * math.pi / 180))
    L = length - length2 * math.sin(18 * math.pi / 180) / math.sin(54 * math.pi / 180)
    for i in range(5):
        star_fractal(x + math.cos((90 + i * 72) * math.pi / 180) * (length - length2),
                     y + math.sin((90 + i * 72) * math.pi / 180) * (length - length2),
                     length2, penc, fillc, n - 1)
# Draw a star fractal with specified parameters
star_fractal(0, 0, 600, 'blue', 'blue', 3)
screen.update()# Update the screen and finish the drawing
turtle.done()
