#Luyi Xiao
#CS5001 & CS5003
#5th, April, 2021

#project 10 npr_scene1.py

import turtle_interpreter
import shapes
import random
import sys

#define a child class,  Mountain
class Mountain(shapes.Shape):
    
    def __init__(self, distance=150, color = (0, 0, 0) ):
        shapes.Shape.__init__(self, distance, 30, color , '{+' + 'F--F++'*8 + '-' + '}')

#new child class, House
class House(shapes.Shape):
    def __init__(self, distance = 40, color = (0, 0, 0)):
        shapes.Shape.__init__(self, distance, 90, color, '{F-(0.5)F-F-(0.5)F-}' + '{y(60)+F(120)-F(120)-F++}')

#new child class, BG1 for background
class BG1(shapes.Shape):
    def __init__(self, distance=800, color = (0, 0, 0)):
        shapes.Shape.__init__(self, distance, 0, color, "F")


#draw the scene when execute the main func
def main():
    #Background:Use dotted style to draw lines contains dots, and cover the dotted line in the background 
    #just as the background of the impressionism 
    bg1 = BG1()
    bg1.setStyle("dotted")
    bg1.setDotSize(5)
    bg1.setJitter(7)

    for i in range(100):
        bg1.setColor((0.8, 0.8+i*0.002, 1-i*0.002)) #make the color like a spectrum- from blue sky to green grass

        bg1.draw(-400, 400-i*8)
        bg1.draw(-399, 399-i*8)

    #several flowers
    flower = shapes.Petal()
    flower.setStyle('jitter')
    for i in range(15):

        pink_color = (1, random.uniform(0.5, 0.7), random.uniform(0.5, 0.7)) #make the color pinky series
        flower.setColor(pink_color)
        flower.draw(random.randint(-350, 380), random.randint(-350, -250), scale=random.uniform(0.7, 0.9))

    #mountains
    mount = Mountain()
    mount.setColor("slategray")
    mount.setStyle("jitter3")
    mount.setWidth(3)

    mount.setJitter(10)
    mount.draw(-400,200)

    #house
    house = House()
    house.setStyle("jitter")
    house.setColor((0.5, 0.1, 0.2))

    for i in range(5):
        house.draw(-200+i*100+random.randint(-50, 50), random.randint(-50, 50), random.uniform(1.2, 1.8))

    #cage: the whole scene is seen from the cage or jail, so I add up the cage in the end using object created using BG1 class
    cage = BG1()
    cage.setWidth(15)
    cage.setStyle('jitter3')
    cage.setJitter(6)
    cage.setColor('black')
    for i in range(5):
        cage.draw(-300+200*i, -400, 1, 90)
    
    #hold
    turtle_interpreter.TurtleInterpreter().hold()



if __name__ == "__main__":
    main()
