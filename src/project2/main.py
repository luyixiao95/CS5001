#Luyi Xiao
#CS5001 2020 Spring, Lab2, main.py
#Feb 1 2021

#import the shape library that contains functions list below:
# goto(x,y); block(x,y, width, length); equ_tri(x,y,size); asterisk(x,y,size)
import shapelib as slib, turtle as t, math, random

#Encapsulate the three shapes in  the shapelib and creat the pic1
def test1():
    slib.block(-50,-50,50,100)
    slib.equ_tri(0,0,50)
    slib.asterisk(100,100,30)

#draw a smily face: the starting locations should be (x0,y0), with certain scales
def test2(x0, y0, scale):
    slib.goto(x0,y0)
#face
    slib.cir(x0, y0 ,scale*50)
#two eyes
    slib.cir(x0-scale*20, y0+scale*60,scale*10)
    slib.cir(x0+scale*20, y0+scale*60,scale*10)
#mouth
    t.right(60)
    slib.arc(x0-10*math.sqrt(3)*scale,y0+30*scale, 20*scale, 120)
    t.left(120)
    t.forward(20*math.sqrt(3)*scale)
#nose
    t.left(60)
    slib.equ_tri(x0,y0+50*scale,15*scale)
    t.left(120)


#draw a scene of lighthouses and houses
def scene1(m,n):
    for i in range(m):
        slib.lighthouse(random.randint(50,150), random.randint(-200,200), random.random())
    for i in range(n):
        j= random.uniform(0.3, 1.2)
        slib.house(random.randint(-300,0), random.randint(-200,200), j*40, j*60)


t.tracer(False)
scene1(2,10)
t.update()
t.mainloop()