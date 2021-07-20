#Luyi Xiao
#CS 5001 & CS 5003
#30th March, 2021
#extensition1.py
import turtle_interpreter
import shapes
import random
import math
#create a hexagon tile
def tile1(x, y, scale):
    hex = shapes.Hexagon(distance = scale, color = (random.random(), random.random(), random.random()))
    hex.draw(x, y+math.sqrt(3)*scale) #To make the lower left part of the shape at the location (x, y)

    petal = shapes.Petal(distance = scale/5, color = (random.random(), random.random(), random.random()))
    koch = shapes.Koch(distance = scale/4, color = (random.random(), random.random(), random.random()))
    pattern_list = [petal, koch]
    pattern = random.choice(pattern_list)
    if pattern == petal:
        petal.draw(x+0.3*scale, y+0.5*scale)
    else:
        koch.draw(x+0.2*scale, y+0.6*scale)
        
#create two triangle tiles
def tile2(x, y, scale):
    tri = shapes.Triangle(distance=scale, color=(random.random(),random.random(),random.random()))
    tri2 = shapes.Triangle2(distance = scale, color = (random.random(), random.random(), random.random()))
    tri.draw(x, y)
    tri2.draw(x, y-scale*math.sqrt(3))


#define a mosaic function that contains only hexagon tiles, this is the first extension image
def mosaic(x, y, scale, Nx, Ny):
    for i in range(Ny):
        for j in range(Nx):
            tile1(x+3/2*scale*j, y+i*scale*math.sqrt(3)+j*scale*1/2*math.sqrt(3), scale)

#define another mosaic function to create an image with hexagon and triangle tiles
def mosaic2(x, y, scale, Nx, Ny):
    for i in range(Ny):
        for j in range(Ny):
            tile1(x+j*scale*2, y+i*scale*math.sqrt(3), scale)
            tile2(x+scale+j*scale*2, y+math.sqrt(3)*scale+math.sqrt(3)*scale*i, scale)

#define test function to create the mosaic image with hexgon tiles
def test1():
    mosaic(-300, -400, 40, 11, 12)
    turtle_interpreter.TurtleInterpreter().hold()

#define test2 function to create the mosaic image with hexgon and triangle tiles
def test2():
    mosaic2(-400, -400, 30, 20, 25)
    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == "__main__":
    test1()
    #run test2() to check my second extension image
    #test2()

