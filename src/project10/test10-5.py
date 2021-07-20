# Bruce Maxwell
# CS 151
# Fall 2010
# Revised Spring 2013
# Revised Fall 2017 for Python 3
# Test function that draws a scene

# Lake with mountains, trees, and clouds, in the background
# Works best with 

import sys
import tree
import shapes
import turtle_interpreter
import random

class BrokenTriangle(shapes.Shape):
    """Mountain class, a broken triangle """
    def __init__(self, size = 20, color = (0.7, 0.75, 0.8) ):
        shapes.Shape.__init__(self, size, 120, color, '{' + ('F(5)-F(5)+'*5 + '+') * 3 + '}')

class TwoBlobs(shapes.Shape):
    """ Cloud class, a broken dual-circle """
    def __init__(self, size = 10, color = (0.97, 0.98, 0.99) ):
        shapes.Shape.__init__(self, size, 10, color, '{' + 'F(18)-'*20 + '}' + '(4)F{' + 'F(18)-'*20 + '}' )

class Grass(shapes.Shape):
    """ Grass, forward and backward """
    def __init__(self, length=1, color = (0.2, 0.3, 0.09) ):
        shapes.Shape.__init__(self, length, 90, color, 'F--F')

    def draw(self, xpos, ypos, scale=1.0, orientation=90 ):
        r = 0.2 + random.gauss(0, 0.02)
        if r < 0.01: r = 0.01
        g = 0.3 + random.gauss(0, 0.02)
        if g < 0.01: g = 0.01
        b = 0.09 + random.gauss(0, 0.02)
        if b < 0.01: b = 0.01

        self.setColor( (r, g, b) )
        shapes.Shape.draw(self, xpos, ypos, scale, orientation )


def main(argv):
    """ main function draws the items into the image
        needs an lsystem tree file to make the trees
    """
    if len(argv) < 2:
        print( 'Usage: python %s <lsystem file>' % (argv[0]))
        exit()

    # background
    s = shapes.Square()
    s.setString( '{F-F-F-F-}' )
    s.setColor( ( 0.88, 0.92, 1.0 ) )
    s.draw( -400, 650, 8 )

    # clouds in the sky
    c = TwoBlobs()
    c.setStyle('jitter')
    c.setJitter( 10 )

    for i in range(6):
        c.draw( random.randint( -450, 400 ), random.randint(200, 400), random.random() + 0.6 )

    # mountains in the background
    m = BrokenTriangle()
    m.setStyle( 'jitter' )
    m.setJitter( 10 )

    for i in [0, 3, 1, 2]:
        m.setColor( ( random.random()*0.05+0.6, random.random()*0.05+0.65, random.random()*0.1+0.7 ) )
        m.draw( -450 + i*150 + random.randint(-10, 10), -200 + random.randint(0, 100), random.random()*0.3 + 2 )

    # grass
    g = Grass()
    g.setStyle( 'jitter' )
    g.setJitter( 3 )

    for i in range(2000):
        g.draw(-450 + random.randint(0,900), random.randint(-450, -200), 4)

    # Trees
    t = tree.Tree( iterations = 3, filename = argv[1] )
    t.setStyle( 'jitter' )

    for i in range(90):
        x = -450 + i*10 + random.randint(-5, 5)
        y = -300 + random.randint(0, 100)
        scale = (y / -300.0 + random.random() * 0.1) * 0.1
        o = 90 + random.randint(-5, 5)
        t.draw( x, y, scale, o )

    # lake
    c.setColor( (0.1, 0.2, 0.8) )
    c.draw( -300, -300, 5, 0 )
    
    # hold
    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == '__main__':
    main(sys.argv)
