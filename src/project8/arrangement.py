#Luyi Xiao
#CS5001 &CS5003
#21 March, 2021
import turtle_interpreter
import lsystem
import sys
import random

#a function to draw at least one L-system tree
def arrangement(sys):
    if len(sys)<2:
        print("please type in more filenames please ")
        exit()
    ti = turtle_interpreter.TurtleInterpreter(800, 800)

    treenum = len(sys)-1
    for i in range(treenum):
        filename = sys[i+1]
        ls = lsystem.Lsystem(filename)

        #SystemGL file needs at least 6 iterations to show the shape of the tree
        if filename == "systemGL.txt":
            tree = ls.buildString(random.randint(6, 7)) 
        else:
        #in other conditions, the L-system iteration 3 to 4 times randomly    
            tree = ls.buildString(random.randint(3, 4))
        #the color of the branches    
        ti.setColor((0.5, 0.4, 0.3))
        ti.setWidth(3)
        #place every tree in a certain place
        ti.place(-300+i*200, -300, 90)
        #the length and angle of "F" are set in a random range
        ti.drawString(tree, random.randint(8, 12), random.randint(12, 25))
    
    ti.hold()

if __name__ == "__main__":
    arrangement(sys.argv)