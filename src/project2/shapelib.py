#luyi xiao
#CS 5001 2021 Spring 
#Lab 2 code file
import turtle as t, random, math
#move turtle to location(x,y)
def goto(x,y):
    t.up()
    t.goto(x,y)
    t.down()

#draw a block by looping

def block(x , y , width, length):
    goto(x,y)
#looping for a block with certain scales and specific height and width 
    for i in range(4):
        if i%2 == 0:
            t.forward(width)
            t.right(90)
        else:
            t.forward(length)
            t.right(90)

#creat a ladder-shaped with one angle of 80, certain scale and starting from x,y
def ladder(x, y, scale):
    goto(x, y)
    t.forward(40*scale)
    t.right(80)
    t.forward(140*scale)
    t.left(80)
    t.backward((40+2*math.sin(10/180*math.pi)*140)*scale)
    t.left(80)
    t.forward(140*scale)
    t.right(80)

#house contains three blocks(rectangles)
def house(x, y, width, length):
    block(x , y, width, length)
    block(x+width/4, y+length/2, width/2, length/2)
    block(x+width/4+width/8,y+length/2+length/4, width/4, length/4)

#creat n houses with random scales of width and length in (50,50)
def random_house(n, width, length):
    for i in range(n):
        j = random.random()
        house(random.randint(-50,50), random.randint(-50,50), j*width, j*length)

#draw a equilateral triangle with certain size
def equ_tri(x, y, size):
    goto(x, y)
    for i in range(3):
        t.forward(size)
        t.left(120)

#draw a asterisk with certain size
def asterisk(x, y , size):
    t.left(90)
    for i in range(5):
        goto(x,y)
        t.forward(size)
        t.left(72)

#draw a circle at a certain radius and the centre at (x,y)

def cir(x,y,radius):
    goto(x,y)
    t.circle(radius)

#draw an arc with certain angle and radius and the centre at (x,y)

def arc(x,y,radius,angle):
    goto(x,y)
    t.circle(radius,angle)

#draw a smily face: the starting locations should be (x0,y0), with certain scales

def smile(x0, y0, scale):
    goto(x0,y0)
#face
    cir(x0, y0 ,scale*50)
#two eyes
    cir(x0-scale*20, y0+scale*60,scale*10)
    cir(x0+scale*20, y0+scale*60,scale*10)
#mouth
    t.right(60)
    arc(x0-10*math.sqrt(3)*scale,y0+30*scale, 20*scale, 120)
    t.left(120)
    t.forward(20*math.sqrt(3)*scale)
#nose
    t.left(60)
    equ_tri(x0,y0+50*scale,15*scale)

#define a lighthouse:
def lighthouse(x0,y0,scale):
    goto(x0,y0)
    ladder(x0,y0,scale)
    block(x0, y0+30*scale, 40*scale, 30*scale)
    equ_tri(x0, y0+30*scale,40*scale)
    goto(x0+scale*20,y0+30*scale+math.sqrt(3)*20*scale)
    t.left(90)
    t.forward(20*scale)
    t.right(90)

#draw a fish
def fish1(x0, y0, scale):
    goto(x0,y0)
    t.right(30)

#body
    t.color("pink")
    t.begin_fill()
    arc(x0, y0, 60*scale, 60)
    arc(x0, y0, -60*scale, 60)
    t.end_fill()

#tail
    t.color("purple")
    t.begin_fill()
    for i in range(3):
        t.forward(20*scale)
        t.left(120)
    t.end_fill()
    t.left(30)

#eye
    t.color("black")
    t.begin_fill()
    cir(x0+10*scale, y0-1*scale, 2*scale)
    t.end_fill()


#draw another type of fish

def fish2(x0, y0, scale):
    goto(x0, y0)

#body
    t.color("orange")
    t.begin_fill()
    t.left(30)
    for i in range(3):
        t.forward(40*scale)
        t.right(120)
    t.end_fill()

    goto(x0+20*math.sqrt(3)*scale, y0)
    t.end_fill()
   
#tail
    t.color("olive")
    t.begin_fill()
    for i in range(3):
        t.forward(20*scale)
        t.right(120)
    t.end_fill()
    t.right(30)

#eye
    t.color("black")
    t.begin_fill()
    cir(x0+10*scale, y0-1*scale, 2*scale)
    t.end_fill()

#draw the third type of fish called manta
def manta(x0, y0, scale):

#body
    goto(x0,y0)
    t.color("grey")
    t.begin_fill()
    t.right(30)
    t.forward(25*scale)
    t.right(120)
    t.forward(50*scale)
    t.left(60)
    t.forward(40*scale)
    t.backward(40*scale)
    t.right(60)
    t.right(60)
    t.forward(50*scale)
    t.right(120)
    t.forward(25*scale)
    t.right(30)
    t.forward(25*math.sqrt(3)*scale)
    t.end_fill()

#eyes
    t.color("black")
    t.begin_fill()
    cir(x0-20*math.sqrt(3)*scale, y0-10*scale, 2*scale)
    t.end_fill()

    t.color("black")
    t.begin_fill()    
    cir(x0-5*math.sqrt(3)*scale, y0-10*scale, 2*scale)
    t.end_fill()

    goto(x0-17.5*math.sqrt(3)*scale, y0-20*scale)
    t.forward(10*math.sqrt(3)*scale)




