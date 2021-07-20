#Luyi Xiao
#CS 5001 & CS 5003
#28th March, 2021
#place.py

import turtle_interpreter as ti
import shapes as sh
import tree 
import sys
import random

#define a function to create an outdoor scene with trees
def scene(argv):
    #Create star and tree object
    star = sh.Koch(20, "yellow")
    tre = tree.Tree(distance =20, iterations = 4, filename=argv[1], width = 3)

    #Use draw method to draw 15 stars with random position above the tree
    for i in range(15):
        star.draw(random.randint(-300, 300), random.randint(200, 300), random.uniform(0.1, 0.5))

    #Use draw method to draw a tree
    tre.draw(0, -300, scale= 1.5)
    
    #draw 10 pedals 
    for j in range(10):
        #for each loop, a new pedal object is made
        #The reason is to make the color random for every pedal
        petal = sh.Petal(15, (random.random(), random.random(), random.random()))
        petal.draw(random.randint(-300, 300), random.randint(-350, -300), random.uniform(0.3, 0.8), random.randint(0, 360))
    ti.TurtleInterpreter().hold()

if __name__ == "__main__":
    scene(sys.argv)

