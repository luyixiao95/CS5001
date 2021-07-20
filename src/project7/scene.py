#Luyi Xiao
#CS5001 & CS 5003
#March 14, 2021
#scene.py
import turtle as t
import turtle_interpreter as ti
import lsystem as ls
import sys
import random
import math

#scene function contains two types of L-systems, a tree and two snowflakes
def scene(sys):
    if len(sys)<1:
        print("There needs to be more elements input from the command line.")
        exit()

    t.setup(500, 500)
    t.tracer(False)
    for element in sys:
        #draw the L-system tree
        if element == "systemD1.txt":
            lsys = ls.createLsystemFromFile(element)
            lstr = ls.buildString(lsys, 4)
            t.up()
            t.left(90)
            t.goto(0, -200)
            t.down()
            t.color(())
            t.width(3)
            ti.drawString(lstr, 7, 22.5)

            ti.initialize()
        
        #draw two koch snowflacks using random package
        elif element == "systemD2.txt":
            lsys = ls.createLsystemFromFile(element)
            #draw 30 snowflacks using for loop
            for i in range(30): 

                #iterate 2 to 5 times randomly
                iteration=random.randint(2, 5) 
                lstr = ls.buildString(lsys, iteration)

                #random the location of the snowflacks
                ti.launch(random.randint(-200, 200), random.randint(-200, 200)) 
                t.color("lightblue")
                t.width(2)
                t.begin_fill()
                #Try some math to let the sizes of different iternation objects similarly
                ti.drawString(lstr, 50/math.pow(iteration, 4) , 60)
                t.fillcolor("lightblue")
                t.end_fill()
                ti.initialize()

    ti.hold()


if __name__ == "__main__":
    scene(sys.argv)

