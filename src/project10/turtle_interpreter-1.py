# Chen Qiu
# CS5003 21Spring
# Lab10
# lsys with parameters
'''
Turtle interpreter
Version4
''' 

import turtle
import random 

class TurtleInterpreter:

    initalized = False

    def __init__(self, dx = 800, dy = 800 ):
        
        self.style='normal'
        self.JitterSigma = 2
        self.dotSize = 2

        if TurtleInterpreter.initalized:
            return TurtleInterpreter.initalized == True 

        turtle.setup( dx, dy )
        turtle.tracer(False)

    # create 3 set methods for Style, JitterSigma, dotsize
    def setStyle(self, s): 
        self.style = s

    def setJitter(self, j):
        self.JitterSigma = j
    def setDotsize( self, d ):
        self.dotSize = d

    # a forward method implements jitter-style drawing
    def forward(self, distance):
        
        if self.style == 'jitter':
            # step 1: store the anchor points and heading        
            x0, y0 = turtle.position()
            turtle.up()
            turtle.forward( distance )
            xf, yf = turtle.position()
            curwidth = turtle.width()
            
            # step 2: set up and draw
            jx = random.gauss( 0, self.JitterSigma )
            jy = random.gauss( 0, self.JitterSigma )
            kx = random.gauss( 0, self.JitterSigma )
            ky = random.gauss( 0, self.JitterSigma )

            turtle.width( curwidth + random.randint(0, 2) )

            turtle.goto(x0 + jx, y0 + jy)
            turtle.down()
            turtle.goto(xf + kx, yf + ky)
            turtle.up()

            # step 3: restore
            turtle.goto(xf, yf)
            turtle.width( curwidth )
            turtle.down()

        # three randomized line segments
        elif self.style == 'jitter3':
            # step 1: store the anchor points and heading        
            x0, y0 = turtle.position()
            turtle.up()
            turtle.forward( distance )
            xf, yf = turtle.position()
            curwidth = turtle.width()
                   
            # step 2: set up and loop
            for i in range(3):
                jx = random.gauss( 0, self.JitterSigma )
                jy = random.gauss( 0, self.JitterSigma )
                kx = random.gauss( 0, self.JitterSigma )
                ky = random.gauss( 0, self.JitterSigma )

                turtle.width(curwidth + random.randint(0, 2))
                
                turtle.goto(x0 + jx, y0 + jy)
                turtle.down()
                turtle.goto(xf + kx, yf + ky)
                turtle.up()
                
            # step 3: restore everything 
            turtle.goto(xf, yf)
            turtle.width( curwidth )
            turtle.down()

        #  draws a series of circles in a line
        elif self.style == 'dotted':
            # step 1: store the anchor points and heading        
            x0, y0 = turtle.position()
            turtle.up()
            turtle.forward( distance )
            xf, yf = turtle.position()
            h_old = turtle.heading()
            curwidth = turtle.width()
            old_color = turtle.color()[0]
            

            # step 2: set up and loop
            dx = xf - x0
            dy = yf - y0
            spacing = self.dotSize*2
            num_dots = int( distance/spacing ) 
            space_size = 1/num_dots # fraction of total distance for each step

            # loop for the number of dots
            for i in range( num_dots ):
                jx = random.gauss( 0, self.JitterSigma )
                jy = random.gauss( 0, self.JitterSigma )
                radius = random.gauss( self.dotSize, self.JitterSigma )
                #print(radius)
                
                # goto the jittered anchor point
                x_dot = x0 + dx*space_size*i + jx
                y_dot = y0 + dy*space_size*i + jy
                turtle.up()
                turtle.goto( x_dot, y_dot )
            	
                # draw dot
                turtle.down()

                turtle.begin_fill()
                cir_color = ( random.random(), random.random(), random.random() ) # normal 
                turtle.color( cir_color )
                turtle.circle( radius )
                turtle.end_fill()
                turtle.up()
                #print( x_dot, y_dot, num_dots, space_size, distance, 'index:', i )
            
            # step 3: restore everything
            turtle.goto( xf, yf )
            turtle.setheading( h_old )
            old_color = turtle.color()[0]
            turtle.down()

        else:
            turtle.forward( distance )

    def drawString( self, dstring, distance, angle):
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
        colorstack = []
        modval = None
        modgrab = False

        for c in dstring:
            if c == "(":
                modgrab = True
                modval = ''
                print( 'modval:', modval )

            elif c == ")":
                modgrab = False
                modval = float(modval)

            elif modgrab:
                print( 'modval:', modval )
                modval += c



            elif c == 'F' or c == 'f':
                if modval == None:
                    self.forward( distance )
                else:
                    self.forward( distance*modval ) 
           
            elif c == '-':
                if modval == None:
                    turtle.right( angle )
                else:
                    turtle.right( modval )

            elif c == '+':
                if modval == None:
                    turtle.left( angle )
                else:
                    turtle.left( modval )

            elif c == '[':
                position = turtle.position()
                stack.append( position )
                heading = turtle.heading()
                stack.append( heading )
            elif c == ']':
                turtle.up()
                pop_heading = stack.pop()
                turtle.setheading( pop_heading )
                pop_position = stack.pop()
                turtle.goto( pop_position )
                turtle.down()


            # width
            elif c == '!':
                if modval == None:
                    w = turtle.width()
                    if w > 1:
                        turtle.width( w-1 )
                else:
                    turtle.width(modval)

            # fill
            elif c == '{':
                turtle.begin_fill()
            elif c == '}':
                turtle.end_fill()

            # add color
            elif c == '<':
                colorstack.append( turtle.color()[0] )
            elif c == '>':
                turtle.color( colorstack.pop() )
            elif c == 'g':
                turtle.color(0.15, 0.5, 0.2)
            elif c == 'y':
                turtle.color(0.8, 0.8, 0.3)
            elif c == 'r':
                turtle.color(0.7, 0.2, 0.3)

            # draw a leaf
            elif c == 'L':
                # set heading
                old_heading = turtle.heading()
                leaf_angle = old_heading + 12
                # set leaf shape
                if leaf_angle > 180:
                    a_leaf = 150  
                elif  leaf_angle > 120:
                    a_leaf = 100 
                else:
                    a_leaf = 180

                self.orient( leaf_angle )

                turtle.begin_fill()
                turtle.circle( distance*0.6, a_leaf )
                turtle.end_fill()

            # add berries
            elif c == 'o':
                turtle.begin_fill()
                turtle.circle( distance*0.16 )
                turtle.end_fill()           
                

        turtle.update()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''
        turtle.hideturtle()
        turtle.update()

        turtle.onkey(turtle.bye, 'q')
        turtle.listen()
        turtle.exitonclick()

    def place( self, xpos, ypos, angle = None ):
        turtle.up()
        turtle.goto( xpos, ypos )
        if angle != None:
            turtle.setheading( angle )
        turtle.down()

    def orient( self, angle ): 
        turtle.setheading( angle )

    def goto(self, xpos, ypos):
        turtle.up()
        turtle.goto( xpos, ypos )
        turtle.down()

    # mutators
    def setColor(self, c): 
        turtle.color(c)

    def setWidth(self, w): 
        turtle.width(w)
    
def test():
    ti= TurtleInterpreter()
    ti.setDotsize(10)
    ti.setJitter(20)
    print( ti.JitterSigma )
    print( ti.dotSize )

if __name__ == '__main__':
    test()