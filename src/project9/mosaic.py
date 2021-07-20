#Luyi Xiao
#CS 5001 & CS 5003
#29th March, 2021
#mosaic.py
import shapes
import turtle_interpreter
import random

#The tile function will make a tile with two pattern randomly with random color
def tile(x, y, scale):
    square = shapes.Square(distance = scale)
    square.draw(x, y+scale, 1, 0)
    petal = shapes.Petal(distance = scale/7, color = (random.random(), random.random(), random.random()))
    koch = shapes.Koch(distance = scale/5, color = (random.random(), random.random(), random.random()))

    #Make a list contains two patterns
    pattern_list = [petal, koch]
    pattern = random.choice(pattern_list)

    if pattern == pattern_list[0]:
        koch.draw(x+scale/5, y+scale/3)
    else:
        petal.draw(x+scale/3, y+scale/4)

#Mosaic function aiming to create a series of tiles at the arrangement of Nx*Ny
def mosaic(x, y, scale, Nx, Ny):

    for i in range(Ny):
        for j in range(Nx):
            tile(x+j*scale, y+i*scale, scale)
    
#define main function to get the mosaic we need
def main():
    mosaic(-200, -200, 100, 5, 4)
    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == "__main__":
    main()

