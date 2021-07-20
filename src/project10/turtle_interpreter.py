#Luyi Xiao
#Revised in 1st April, 2021
#CS5001 & CS5003
#turtle_interpreter.py version 4

import turtle as t
import random 
#define a new class called TurtleInterpreter
class TurtleInterpreter:

    #Use this in global class to make only one window can be created
    initialized = False

    def __init__(self, dx = 800, dy = 800):

        #set style and jitterSigma fields to use in NPR
        self.style = 'normal'
        self.jitterSigma = 2
        self.dotSize = 1  #radius of every dot
        self.width = 1
        self.brush_lenth = 2
        self.brush_num = 10
        if TurtleInterpreter.initialized:
            return None
        TurtleInterpreter.initialized = True        
        t.setup(dx, dy)

    #Get style field
    def getStyle(self):
        return self.style
    
    #Set style to s
    def setStyle(self, s):
        self.style = s
    
    #Get jitterSigma

    def getJitter(self):
        return self.jitterSigma
    
    #reset jitterSigma
    def setJitter(self, j):
        self.jitterSigma = j

    #reset dotSize
    def setDotSize(self, d):
        self.dotSize = d

    #reset width
    def setWidth(self, w):
        self.width = w

    #reset the brush_lenth
    def setBrushlength(self, b):
        self.brush_lenth = b

    #reset brush_num
    def setBrushNum(self, b):
        self.brush_num = b

    #revised forward method
    def forward(self, distance):

        if self.style == "jitter":
            #draw a jittered line
            x0, y0 = t.position()
            t.up()
            t.forward(distance)
            xf, yf = t.position()
            curwidth = t.width() 
            
            #set jx, jy, kx, ky
            jx =  random.gauss(0, self.jitterSigma)
            jy =  random.gauss(0, self.jitterSigma)
            kx =  random.gauss(0, self.jitterSigma)
            ky =  random.gauss(0, self.jitterSigma)

            t.width(curwidth+random.randint(0, 2)) #Why not self.width + random.randint(0, 2)

            t.goto(x0 + jx, y0 + jy)
            t.down()
            t.goto(xf + kx, yf + ky)
            t.up()
            t.goto(xf, yf)
            t.width(curwidth)
            t.down()
        elif self.style == "jitter3":
        #Design the jitter3 style
            #Part 1:
            x0, y0 = t.position()
            t.up()
            t.forward(distance)
            xf, yf = t.position()
            curwidth = t.width()
            curcol = t.color()[0]
            curhead = t.heading()

            #Part 2:
            
            for i in range(3):
                jx = random.gauss(0, self.jitterSigma)
                jy = random.gauss(0, self.jitterSigma)
                kx = random.gauss(0, self.jitterSigma)
                ky = random.gauss(0, self.jitterSigma)
                ran_color = (random.random(), random.random(), random.random())

                t.width(self.width+random.randint(0, 2))
                if curcol == (0, 0, 0):
                    t.color(ran_color)
                t.goto(x0 + jx, y0 + jy)
                t.down()
                t.goto(xf + kx, yf + ky)
                t.up()
            
            #Part 3
            t.goto(xf, yf)
            t.width(curwidth)
            t.color(curcol)
            t.setheading(curhead)
            t.down()
        
        elif self.style == "dotted":
            #part 1
            t.up()
            x0, y0 = t.position()
            t.forward(distance)
            xf, yf = t.position()
            col = t.color()[0]
            head = t.heading()

            #Part 2
            radius = self.dotSize
            dot_number = int(distance/(4*radius)) #to set dots devide a radius length
            for i in range(dot_number):
                jx = random.gauss(0, self.jitterSigma)
                jy = random.gauss(0, self.jitterSigma)
                rr = random.gauss(0, self.jitterSigma)
                if col == (0, 0, 0):
                    t.color((random.random(), random.random(), random.random()))
                t.goto(x0, y0)
                t.forward(i*4*radius)
                x, y = t.position()
                t.goto(x+jx, y+jy) #move to the center of a dot
                t.down()
                t.begin_fill()
                t.circle(radius + rr) #draw a circle
                t.end_fill()
                t.setheading(head)
                t.up()
            
            #part 3
            t.goto(xf, yf)
            t.color(col)
            t.setheading(head)
            t.down()
        
        #found a new style:brush
        elif self.style == "brush":
            #part 1
            x0, y0 = t.position()
            t.forward(distance)
            xf, yf = t.position() #in this style, we might directly draw the main line in a certain postion
            t.up()  
            col = t.color()[0]
            head = t.heading()
            width = t.width()

            #part 2

            t.goto(x0, y0)
            t.goto(xf, yf) 
            t.up() 
            num = self.brush_num
            length = self.brush_lenth
            dx = (xf-x0)/num
            dy = (yf-y0)/num
            t.left(90)

            for i in range(num):
                #ideal start point of every brush position xs, ys
                xs = x0 + i*dx
                ys = y0 + i*dy

                t.goto(xs, ys)
                t.forward(length)
                #ideal end point 
                xe, ye = t.position()
                jx = random.gauss(0, self.jitterSigma)
                jy = random.gauss(0, self.jitterSigma)
                kx = random.gauss(0, self.jitterSigma)
                ky = random.gauss(0, self.jitterSigma)
                t.goto(xs+jx, ys+jy)
                
                #set the color and width
                r, g, b = col
                newc = []
                for i in [r, g, b]:
                    i = i + random.gauss(0, 0.15)
                    i = min(max(i, 0), 1)
                    newc.append(i)

                t.color(tuple(newc))
                t.width(self.width)

                
                #draw the brush
                t.down()
                t.goto(xe+kx, ye+ky)
                t.up()

            #part 3
            t.goto(xf, yf)
            t.setheading(head)
            t.width(width)
            t.color(col)
            t.down()

        else:   #other types of styles are considered as normal style
            origin_wid = t.width()
            t.width(self.width)
            t.forward(distance)
            t.width(origin_wid)


    
    #drawstring method using turtle package to draw the L-system loads into the method
    def drawString(self, dstring, distance, angle):
        modval = None
        modgrab = False

        t.tracer(False)
        stack = []
        colorstack = []
        for c in dstring:
            if c == "(":
                modgrab = True
                modval = ""
                continue

            elif c == ")":
                modgrab = False
                modval = float(modval)
                continue

            elif modgrab:
                modval += c
                continue
            else:
                if c == "F" or c == "f":
                    if modval == None:
                        self.forward(distance)
                    else:
                        self.forward(distance*modval)


                elif c == "-":
                    if modval == None:
                        t.right(angle)
                    else:
                        t.right(modval)

                elif c == "+":
                    if modval == None:
                        t.left(angle)
                    else:
                        t.left(modval)

                elif c == "!":
                    if modval == None:
                        w = t.width()
                        if w > 1:   
                            t.width(w-1)

                    else:
                        t.width(modval)


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
                elif c == "{":
                    t.begin_fill()

                elif c == "}":
                    t.end_fill()

                elif c == "X":
                    origin_color = t.color()[0]
                    t.color("green")
                    t.begin_fill()
                    t.circle(2)
                    t.fillcolor()
                    t.end_fill()
                    t.color(origin_color)
                
                elif c == "l":
                    origin_color = t.color()[0]
                    t.color("red")
                    t.begin_fill()
                    t.circle(3)
                    t.fillcolor()
                    t.end_fill()
                    t.color(origin_color)
                elif c == "|":  #reverse direction
                    t.left(180)

                elif c == "^": #set the heading to 0
                    t.setheading(0)

                modval = None
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

    #set the background color of a given graph
    def backcolor(self, color):
        t.bgcolor(color)

    #type in some words in a given graph
    def write(self, words):
        t.write(words, False, "center", font= ("Arial", 16))

