#Luyi Xiao
#CS5001 & CS5003
#6th, April, 2021
#npr_scene2.py

import turtle_interpreter
import shapes
import tree
import sys
import random

#create child class Spiral
class Spiral(shapes.Shape):
    def __init__(self, distance=1, color = "gold"):
        istring = ""
        for i in range(80):
            j=str(1+0.3*i)
            istring += "+(" + j + ")"+ "F" 

        shapes.Shape.__init__(self, distance, 20, color, istring) 
#Create child class Building
class Building(shapes.Shape):
    def __init__(self, distance =30, color = (0, 0, 0)):
        shapes.Shape.__init__(self, distance, 90, color, istring="{F(4)-F(4)-F(4)-FF(10)-FF(20)+FF(160)-F(120)+F(30)+FFF(140)-FFF(20)-FF(5)-FF(5)-FFFFF}")

#creat child class BG2 as the background of the tree
class BG2(shapes.Shape):
    def __init__(self, distance = 800, color = (0, 0, 0)):
        shapes.Shape.__init__(self, distance, 0, color, "F")

def main(argv):
    #Background
    bg2 = BG2()
    bg2.setStyle("jitter3")
    bg2.setJitter(15)
    for i in range(400):
        bg2.setColor((0.1, 0.1+i*0.001, 0.20+i*0.002)) #let the color gradually changes 
        bg2.draw(-400, 400-i*2)
    #spiral
    spiral = Spiral()
    spiral.setWidth(5)
    spiral.setStyle("jitter3")

    spiral.draw(-200, 200)
    spiral.draw(50, 180, 0.8)
    spiral.draw(250, 190, 0.6)
    #trees
    tre1 = tree.Tree(distance=1, filename = argv[1], iterations=4)
    tre1.setStyle("normal")
    tre1.setWidth(3)
    tre1.setJitter(1)    
    tre1.draw(0, -300, 0.5)
    tre2 = tree.Tree(distance=1, filename = argv[2])
    tre2.setStyle("jitter")
    tre2.setJitter(1)
    for i in range(10):
        tre2.draw(-300+i*70, -300+random.gauss(0, 25), 0.6)

    #stars
    cir = shapes.Circle()
    cir.setColor("lightsteelblue")
    cir.setStyle("jitter")
    for i in range(5):
        cir.draw(-300+150*i+random.randint(-50,50), 250+random.randint(-200, 200), random.uniform(0.2, 0.3))

    #buliding
    building = Building()
    building.setColor("dimgray")
    building.setStyle("jitter")
    building.setJitter(5)
    building.draw(-380, -400, 1.5)

    #hold
    turtle_interpreter.TurtleInterpreter().hold()

#execute the main()
if __name__ == "__main__":
    main(sys.argv)