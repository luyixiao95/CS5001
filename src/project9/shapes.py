#Luyi Xiao
#CS 5001 & CS 5003
#26th March, 2021
#shapes.py

import turtle_interpreter
#define a parent class shapes
class Shape:
    #Shape contains fields: distance, angle, color and string
    def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring= ""):
        self.distance = distance
        self.angle = angle
        self.color = color
        self.string = istring
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
    #draw method to use turtle interpreter to draw an object
    def draw(self, xpos, ypos, scale = 1.0, orientation = 0):
        TI = turtle_interpreter.TurtleInterpreter()
        TI.place(xpos, ypos, orientation)
        TI.setColor(self.color)
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
        Shape.__init__(self, distance, 3.6 , color, "F-"*100)

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
    


