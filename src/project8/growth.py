#Luyi Xiao
#21 March, 2021
#CS5001 & CS5003
#Project 8: growth.py

import turtle_interpreter
import lsystem
import sys
import random

#define a grow function to draw the L-system we created
def grow(sys):
    #use for loop to draw three trees
    for i in range(4, 7):

        ls = lsystem.Lsystem(sys[1])
        lstring = ls.buildString(i)
        ti = turtle_interpreter.TurtleInterpreter()
        ti.backcolor("lightblue")
        ti.setColor((0.6, 0.5, 0.4))
        ti.setWidth(3)
        #place the three trees in order
        ti.place(-200+(i-4)*200, -350, 90)
        ti.drawString(lstring, 3, 22.5)
    
    #draw some sparking points to decorate the graph
    for j in range(100):
        ti.place(random.randint(-350, 350), random.randint(-350, 350))
        ti.drawString("X", 2, 0) 

    ti.hold()

if __name__ == "__main__":
    grow(sys.argv)