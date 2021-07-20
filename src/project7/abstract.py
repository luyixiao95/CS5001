#Luyi Xiao
#CS 5001 & CS5003
#Mar 13, 2021
#Project 7:abstract.py

import turtle as t
import turtle_interpreter as ti
import lsystem as ls
import sys


#A function contains three L-systems

def abstract(sys):
    if len(sys) < 0:
        print("")
        exit()

    t.setup(500, 500)
    t.tracer(False)
    for element in sys[1:]:
        if element == "systemA1.txt" :
            lsys1 = ls.createLsystemFromFile(element)
            lstr1 = ls.buildString(lsys1, 3)

            t.up()
            t.goto(0, 200)
            t.down()
            t.color("blue")
            t.width(3)
            ti.drawString(lstr1, 20, 120)
            t.setheading(0)
        
        if element == "systemA2.txt":
            for i in range(3):
                t.up()
                t.goto(10, -10)
                t.left(i*120)
                t.down()
                lsys2 = ls.createLsystemFromFile(element)
                lstr2 = ls.buildString(lsys2, 2)
                t.color("pink")
                t.width(3)
                ti.drawString(lstr2, 15, 90)
                t.setheading(0)

        if element == "systemC1.txt":
            lsys3 = ls.createLsystemFromFile(element)
            lstr3 = ls.buildString(lsys3, 5)
            t.up()
            t.left(90)
            t.goto(0, -100)
            t.down()
            t.color("green")
            t.width(2)
            ti.drawString(lstr3, 5, 20)
            t.setheading(0)


        

    ti.hold()


if __name__ == "__main__":
    abstract(sys.argv)

