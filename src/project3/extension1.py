#Luyi Xiao
#CS 5001, project 3, extension.py
#9th, Feb, 2021

#using simple coding to bulid a very complex shape
import turtle as t, random

#firstly define a function to draw a n-side-polygon
def n_gon(side, width, scale):
    for i in range(side):
        t.fd(scale*width)
        t.left(360/side)

#Define the Kaleidoscope funct
def Kalei(scale, number, fill, pensize):
    for i in range(number):
        if fill: 
            random_color=(random.random(), random.random(), random.random())  #random color
            random_side= random.randint(3, 10) #the basic element in the Kaleidoscope is from triangle to enneagon 
            t.color(random_color) 
            t.pensize(pensize)
            t.begin_fill()
            t.up()
            t.circle((50+ i*5) *scale , 10) #spiral trace of the basic element 
            t.down()
            n_gon(random_side, 100, scale)




t.tracer(False)
Kalei(0.5, 150, True, 4)
t.update()


t.mainloop()
    