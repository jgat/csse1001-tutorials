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
    i = 0
    while i < sides:
        turtle.forward(20 * (i / 2 + 1))
        turtle.left(90)
        i += 1

def interact():
    turtle.reset()
    distance = int(raw_input("Distance: "))
    while True:
        cmd = raw_input("Direction: ")
        if cmd == 'e':
            turtle.setheading(0)
        elif cmd == 'n':
            turtle.setheading(90)
        elif cmd == 'w':
            turtle.setheading(180)
        elif cmd == 's':
            turtle.setheading(270)
        elif cmd == 'q':
            turtle.bye()
            break
        else:
            print "That's not a direction"
            continue
        turtle.forward(distance)
