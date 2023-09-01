import random
import turtle
colors=["red", "orange", "yellow", "green", "blue", "purple"]
t = turtle.Turtle()
psize =15
size = 5
for _ in range(45):
    color = random.choice(colors)
    t.pencolor(color)
    t.forward(size)
    t.right(15)
    size += 4
    t.pensize(psize + 2)
    t.left(60)
turtle.done()
