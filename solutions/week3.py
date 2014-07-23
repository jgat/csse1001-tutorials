# We will need the turtle library and the math library.
import turtle
import math
# Can also be written:
# import turtle, math

def rectangle(a, b):
    """
    Draws a rectangle with the given side lengths (width, height), with
    cursor pointing east once finished.
    (a, b) = (width, height)

    Leaves cursor pointing in the same direction as it was found.

    rectangle(int, int) -> None
    """

    # Draw the bottom edge
    turtle.forward(a)
    # Rotate 90 degrees
    turtle.left(90)

    # Draw the right edge
    turtle.forward(b)
    # Rotate 90 degrees
    turtle.left(90)

    # Draw the top edge
    turtle.forward(a)
    # Rotate 90 degrees
    turtle.left(90)

    # Draw the left edge
    turtle.forward(b)
    # Rotate 90 degrees (i.e. finish pointing east)
    turtle.left(90)

    turtle.exitonclick()


def rotated_rectangle(a, b, angle):
    """
    Draws a rotated rectangle with the given side lengths (width, height),
    rotated by angle, with cursor pointing east once finished.
    (a, b) = (width, height)

    Leaves cursor pointing in the same direction as it was found.

    rotated_rectangle(int, int, int) -> None
    """
    # Rotate left by angle
    turtle.left(angle)
    # Draw a rectangle, using our rotated (east) cursor
    rectangle(a, b)
    # Rotate right by angle (i.e. point east again)
    turtle.right(angle)

    turtle.exitonclick()


def polygon(size, n):
    """
    Draws a polygon with n sides, and each side having length specified by
    size.

    Leaves cursor pointing in the same direction as it was found.

    polygon(int, int) -> None
    """
    side = size * math.sin(math.pi / n)
    i = 0
    while i < n:
        turtle.forward(side)
        turtle.left(360. / n)
        i += 1

    turtle.exitonclick()


def spiral(sides):
    """
    Draws a square spiral with a number of lines specified by sides.

    spiral(int) -> None
    """
    i = 0
    while i < sides:
        turtle.forward(20 * (i / 2 + 1))
        turtle.left(90)
        i += 1

    turtle.exitonclick()


def interact():
    turtle.reset()

    # Prompt the user for a distance
    distance = int(raw_input("Distance: "))

    while True:
        # Prompt the user for a direction
        cmd = raw_input("Direction: ")

        # Handle each command.
        if cmd == 'e':
            # Tell turtle to head east.
            turtle.setheading(0)
        elif cmd == 'n':
            # Tell turtle to head north.
            turtle.setheading(90)
        elif cmd == 'w':
            # Tell turtle to head west.
            turtle.setheading(180)
        elif cmd == 's':
            # Tell turtle to head south.
            turtle.setheading(270)
        elif cmd == 'q':
            # Quit
            turtle.bye()
            break
        else:
            # Inform the user that they have not entered a valid direction.
            print "That's not a direction"
            # Do not move forward since no valid direction was given.
            continue
            # ---------------------------------------------------------------
            # The continue keyword skips immediately to the end of the
            # currently iteration of the loop and will proceed into the loop
            # again if the condition is met. Contrast with break, which will
            # immediately exit the loop, whereas continue skips to the end
            # of the current iteration.
            # ---------------------------------------------------------------

        # Move the distance that the user previously specified.
        turtle.forward(distance)

        turtle.exitonclick()
