import turtle
import math

def rectangle(a, b):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)

def rotated_rectangle(a, b, angle):
    turtle.left(angle)
    rectangle(a, b)
    turtle.right(angle)

def polygon(size, n):
    side = size * math.sin(math.pi / n)
    i = 0
    while i < n:
        turtle.forward(side)
        turtle.left(360. / n)
        i += 1

def spiral(sides):
    turtle.reset()
    i = 0
    while i < sides:
        turtle.forward(20 * (i / 2 + 1))
        turtle.left(90)
        i += 1
