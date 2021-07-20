#Luyi Xiao
#27th March, 2021
#CS 5001& CS5003
#tree.py

import lsystem as ls
import shapes as sh
import sys
import turtle_interpreter  as ti


#Define a tree class
class Tree(sh.Shape):

    def __init__(self, distance = 5, angle = 22.5, color = (0.5, 0.4, 0.3), iterations=3, filename = None, width = 1):
        sh.Shape.__init__(self, distance, angle, color)
        self.iterations = iterations
        self.lsys = ls.Lsystem(filename)
        self.width = width 

    def setIterations(self, N):
        self.iterations = N
    
    def read(self, filename):
        self.lsys.read(filename)

    
    #override the draw method
    def draw(self, xpos, ypos, scale=1.0, orientations=90):
        #set the width of the turtle pen
        ti.TurtleInterpreter().setWidth(self.width)
        self.string = self.lsys.buildString(self.iterations)
        sh.Shape.draw(self, xpos, ypos, scale, orientations)

#test the tree class
def test(argv):
    #creat a tree object
    tre = Tree(distance=30, color="gray", filename = argv[1])
    #use draw method to draw three trees
    tre.draw(-200, -100)
    tre.draw(0, -100)
    tre.draw(200, -100)
    #hold
    ti.TurtleInterpreter().hold()


if __name__ == "__main__":
    test(sys.argv)






