#Luyi Xiao
#CS 5001 & CS 5003
#March 14, 2021
#grid.py

import turtle as t
import lsystem as ls
import turtle_interpreter as ti
import sys

#function grid contains 9 trees in a 3*3 grid

def grid(sys):
    if len(sys)<2:
        print("There need to be at least two files inputting")
        exit()

    lsys = ls.createLsystemFromFile(sys[1])
    t.setup(500, 500)
    t.tracer(False)
    t.color("green")
    t.width("2")
    
    #nested for loop to consider the 3*3 grid 
    for row in range(3):
        for col in range(3):
            t.left(90)
            ti.launch(-200 + col*150, -220 + row*180)
            iter = int(col + 1) 
            angle = 22-5*row*row+29*row #when row = 0, angle = 22; row = 1, angle = 46; row = 2, angle = 60 
            lstr = ls.buildString(lsys, iter)
            ti.drawString(lstr, 5, angle)
            t.setheading(0)

            
            
    ti.hold()
        
if __name__ == "__main__":
    grid(sys.argv)

