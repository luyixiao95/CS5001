#LUyi Xiao
#19 March, 2021
#CS5001 & CS5003
#turtle_interpreter.py version 2

import turtle as t
import random 

#define a new class called TurtleInterpreter
class TurtleInterpreter:

    def __init__(self, dx = 800, dy = 800):
        t.setup(dx, dy)
        t.tracer(False)
        t.hideturtle()
    
    #drawstring method using turtle package to draw the L-system loads into the method
    def drawString(self, dstring, distance, angle):
        stack = []
        colorstack = []
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
            elif c == "<":
                colorstack.append(t.color()[0])
            elif c == ">":
                col = colorstack.pop()
                t.color(col)
            elif c == "g":
                t.color(0.15, 0.5, 0.2)
            elif c == "y":
                t.color(0.8, 0.8, 0.3)
            elif c == "r":
                t.color(0.7, 0.2, 0.3)
            elif c == "L":
                t.begin_fill()
                t.circle(3)
                t.fillcolor(t.color()[0])
                t.end_fill()
            elif c == "X":
                t.color(random.random(), random.random(), random.random())
                t.begin_fill()
                t.circle(2)
                t.fillcolor()
                t.end_fill()

        t.update()

    def hold(self):
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

    #place the turtle to the given position and angle
    def place(self, xpos, ypos, angle = None):
        t.up()
        t.goto(xpos, ypos)
        if angle:
            t.setheading(angle)
        t.down()

    #turn to some certain angle
    def orient(self, angle):
        t.setheading(angle)

    #turtle to a given position 
    def goto(self, xpos, ypos):
        t.up()
        t.goto(xpos, ypos)
        t.down()

    #set the color of a turtle
    def setColor(self, c):
        t.color(c)
    
    #set the width of the turtle pensize
    def setWidth(self, w):
        t.width(w)

    #set the background color of a given graph
    def backcolor(self, color):
        t.bgcolor(color)

    #type in some words in a given graph
    def write(self, words):
        t.write(words, False, "center", font= ("Arial", 16))