#Luyi Xiao
#CS 5001 & CS 5003
#26th March, 2021
#shapes.py

import turtle_interpreter
#define a parent class shapes
class Shape:
    #Shape contains fields: distance, angle, color and so on
    def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring= "", style = "normal", jitterSigma = 2, width = 1, dotSize = 1, brush_lenth=2, brush_num = 10):
        self.distance = distance
        self.angle = angle
        self.color = color
        self.string = istring
        self.style = style
        self.jitterSigma = jitterSigma
        self.width = width
        self.dotSize = dotSize
        self.brush_lenth = brush_lenth
        self.brush_num = brush_num
        
    #setColor method to set the color of the object
    def setColor(self, c):
        self.color = c
    #setDistance method to set the distance of the object
    def setDistance(self, d):
        self.distance = d
    #setAngle method to set the angle of the object
    def setAngle(self, a):
        self.angle = a
    #setString method to set the string of the object
    def setString(self, s):
        self.string = s
    #get the style field
    def getStyle(self):
        return self.style
    #set the style field    
    def setStyle(self, s):
        self.style = s
    #set the dotsize
    def setDotSize(self, d):
        self.dotSize = d
    #get the number of jitterSigma
    def getJitter(self):
        return self.jitterSigma
    #set the jitterSigma
    def setJitter(self, j):
        self.jitterSigma = j
    #get the width of the turtle
    def getWidth(self):
        return self.width
    #reset the width of the turtle
    def setWidth(self, w):
        self.width = w
    #reset the brush_length 
    def setBrushlength(self, b):
        self.brush_lenth = b
    #reset the brush_num
    def setBrushNum(self, b):
        self.brush_num = b
    #draw method to use turtle interpreter to draw an object
    def draw(self, xpos, ypos, scale = 1.0, orientation = 0):
        TI = turtle_interpreter.TurtleInterpreter()
        TI.place(xpos, ypos, orientation)
        TI.setColor(self.color)
        TI.setStyle(self.style)
        TI.setJitter(self.jitterSigma)
        TI.setWidth(self.width)
        TI.setDotSize(self.dotSize)
        TI.setBrushlength(self.brush_lenth)
        TI.setBrushNum(self.brush_num)
        TI.drawString(self.string, self.distance*scale, self.angle)

#Child class: Square
class Square(Shape):
    #field using the parent class
    def __init__(self, distance = 100, color = (0, 0, 0)):
        Shape.__init__(self, distance, 90, color, "F-F-F-F-")

#Child class: Triangle
class Triangle(Shape):
    def __init__(self, distance = 100, color = (0, 0, 0)):
        Shape.__init__(self, distance, 120, color, "{F-F-F-}")

#Child class: Triangle2
class Triangle2(Shape):
    def __init__(self, distance = 100, color = (0, 0, 0)):
        Shape.__init__(self, distance, 120, color,  "{F+F+F+}")

#Three more child classes for the project
#Child class Hexagon
class Hexagon(Shape):
    def __init__(self, distance = 50, color= (0, 0, 0) ):
        Shape.__init__(self, distance, 60, color, "F-F-F-F-F-F-")

#Child class Circle
class Circle(Shape):
    def __init__(self, distance = 5 , color = (0, 0, 0)):
        Shape.__init__(self, distance, 3.6 , color, "{" + "F-"*100 + "}")

#Child class koch(snowflake)
class Koch(Shape):
    def __init__(self, distance = 30, color = (0, 0, 0)):
        Koch_base = "{F++F++F}"
        Koch_rule = "F-F++F-F"
        kouch_str = Koch_base.replace("F", Koch_rule) 
        Shape.__init__(self, distance, 60, color, kouch_str+"++")

#Class Petal
class Petal(Shape):
    def __init__(self, distance = 20, color = (0, 0, 0)):
        petal_base = "{F++F++F++F++F}"
        petal_rule = "F++F++F|F-F++F"
        petal_str = petal_base.replace("F", petal_rule)
        Shape.__init__(self, distance, 36, color, petal_str+"++")
        turtle_interpreter.TurtleInterpreter().orient(0)


#define a test function to draw three extensional classes
def test():
    hex = Hexagon()
    cir = Circle()
    koc = Koch()
    petal = Petal()
    hex.draw(-100, -100)
    cir.draw(-200, 200)
    koc.draw(100, 0)
    petal.draw(200, 0)



    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == "__main__":
    test()
    


