# Bruce Maxwell
# CS 5001 Project 7
# Fall 2020
# First L-system project
# Some test code that draws 3 simple shapes

import turtle as t
import turtle_interpreter as ti

# a simple goto function
def goto(x, y):
    t.up()
    t.goto(x, y)
    t.down()

# main function, create some simple shapes
def makeShapes():
    t.setup(500, 500)

    # turn off tracing
    t.tracer(False)

    # draw a triangle
    goto( -100, 0)
    s = 'F+F+F+'
    t.color( 'blue' )
    ti.drawString( s, 65, 120 )

    # draw a square
    goto( 0, 0 )
    s = 'F+F+F+F+'
    t.color( 'red' )
    ti.drawString( s, 50, 90 )

    # draw a pentagon
    goto( 100, 0 )
    s = 'F+F+F+F+F+'
    t.color( 'green' )
    ti.drawString( s, 40, 72 )

    # update the window and hold
    ti.hold()

    return


if __name__ == "__main__":
    makeShapes()
    
