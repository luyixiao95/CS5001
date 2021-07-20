#Luyi Xiao 
#7th April, 2021
#CS5001 &CS5003
#extension1.py

import turtle_interpreter
import shapes
#main function to draw a square with brush type
def main():
    squ = shapes.Square(distance=300) #create a new object
    squ.setStyle("brush") #reset style to brush
    squ.setWidth(1.5)  #reset the width to 1.5
    squ.setJitter(1)    
    squ.setColor((0.2, 0.3, 0.5))
    squ.setBrushlength(30) #brush length 30
    squ.setBrushNum(15)  #number of brush 15
    squ.draw(-100, 100)

    turtle_interpreter.TurtleInterpreter().hold()

#execute main funct.
if __name__ == "__main__":
    main()

