#Luyi Xiao
#CS5001 & 5003
#Mar 13, 2021
#Project 7

import turtle as t

#draw each element in the L-system
def drawString(dstring, distance, angle):
    """ Interpret the characters in string dstring as a series
    of turtle commands. Distance specifies the distance
    to travel for each forward command. Angle specifies the
    angle (in degrees) for each right or left command. The list of 
    turtle supported turtle commands is:
    F : forward
    - : turn right
    + : turn left
    [ : save the turtle's heading and position
    ] : restore the turtle's heading and position
    """
    stack = []
    for c in dstring:
        if c == "F":
            t.forward(distance)
        elif c == "-":
            t.right(angle)
        elif c == "+":
            t.left(angle)
        elif c == "[":
            stack.append(t.position())
            stack.append(t.heading())
        elif c == "]":
            t.up()
            t.setheading(stack.pop())
            t.goto(stack.pop())
            t.down()
    t.update()


def hold():
    '''Holds the screen open until user clicks or presses 'q' key'''

    # Hide the turtle cursor and update the screen
    t.hideturtle()
    t.update()

    # Close the window when users presses the 'q' key
    t.onkey(t.bye, 'q')

    # Listen for the q button press event
    t.listen()

    # Have the turtle listen for a click
    t.exitonclick()


#define a function to initialize the turtle after a L-system is drawn
def initialize():
    t.up()
    t.home()
    t.down()

#launch function to move the turtle to a certain (x, y)
def launch(x, y):
    t.up()
    t.goto(x, y)
    t.down()