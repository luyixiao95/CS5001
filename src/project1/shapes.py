#Luyi Xiao
#CS 5003 Project 1, shapes.py, 
#Jan 26, 2021
from turtle import *
#define equ_triangle() that can create an equilateral triangle. Input certain number can bulid the shape with certain length
def equ_triangle(length):
    forward(length)
    left(120)
    forward(length)
    left(120)
    forward(length)
    left(120)
#define square() that can create a square. Input a certain number can create the shape with certain length
def square(length):
    forward(length)
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)

#define cir() that can create a square and input a certain number can creat a circle with certain radius
def cir(length):
    circle(length)

#define test() to call three shape functions twice using different arguments (sizes)

def test(size1, size2):
    equ_triangle(size1)
    equ_triangle(size2)

    up()
    right(90)
    forward(20)
    left(90)
    down()

    square(size1)
    square(size2)

    up()
    backward(100)
    down()

    cir(size1)
    cir(size2)

#define a composite shape function that contains all three shapes
def composite(scale):
    equ_triangle(50*scale)
    square(50*scale)
    
    up()
    right(90)
    forward(50*scale)
    left(90)
    forward(25*scale)
    down()
    cir(25*scale)

def scene():
    composite(1.0)
    up()
    right(90)
    forward(50)
    down()
    equ_triangle(30)
    square(30)
    cir(30)

scene()
mainloop()
