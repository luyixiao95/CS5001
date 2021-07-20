#Luyi Xiao
#CS 5001, project 3, newshapelib.py
#7th, Feb, 2021
#Revision on 16th, March, 2021 for project 7, L-system
#two L-system trees are added

import turtle as t, random, math
import lsystem as ls
import turtle_interpreter as ti
import sys


#define a function that the turtle can goto (x, y) straightfowardly without using penup and pendown:
def launch(x, y):
    t.up()
    t.goto(x, y)
    t.down()


#define a block function that contains x, y, width, height, fill, color
def block(x,y, width, height, fill, color):
    launch(x, y)
    if fill:
        t.color(color)
        t.begin_fill()
        for i in range(2):
            t.fd(width)
            t.left(90)
            t.fd(height)
            t.left(90)
    t.end_fill()

#define a ring with x, y, radius, pinsize, fill, and pencolor
def ring(x, y, r, pinsize, color):
    launch(x,y)
    t.pensize(pinsize)
    t.pencolor(color)
    t.circle(r)


#define a n_gon with n sides, x, y to start, certain width fill and color
def n_gon(n, x, y, width, fill, color):
    launch(x, y)
    if fill:
        t.color(color)
        t.begin_fill()
        for i in range(n):
            t.forward(width)
            t.left(360/n)
        t.end_fill()


#Define an Olympic ring, which contains five rings. Three parameters (x, y and scale) are used
def oly_ring(x, y, scale):
    for i in range(5):
        ring_color= ["blue", "black", "red", "yellow", "green"]
        if i<3:
            ring(x+i*120*scale, y, 50*scale, 10*scale, ring_color[i])
        else:
            ring(x+60*scale+(i-3)*120*scale, y-50*scale, 50*scale, 10*scale, ring_color[i])


#Define a necessary aggregate shape: tree, using basic shapes

def tree(x, y, scale, sys):
    t.pensize(1)
    lsys=ls.createLsystemFromFile(sys[1])
    lstr=ls.buildString(lsys, 3)
    ti.launch(x*scale, y*scale)
    t.left(90)
    t.color("green")
    ti.drawString(lstr, 4*scale, 22.5)
    ti.initialize()
    


#Define a rostrum that can let the winner standing on it

def rostrum(x, y, width, scale, fill, color):
    list_of_height = [0.5, 1.2, 0.3]
    for i in range(3):
        block(x+i*width*scale, y, width*scale, list_of_height[i]*width*scale, fill, color)


#define different types of fireworks

def fireworks(x, y, side, width, scale, fill, color, pensize):
    launch(x,y)
    t.pensize(pensize)
    if fill:
        t.color(color)
        for i in range(side):
            t.up()
            t.fd(width*scale/2)
            t.down()
            t.fd(width*scale/2)
            t.up()
            t.backward(width*scale)
            t.down()
            t.right(360/side)



#draw three different types of fishes (Originally from project 2, and they are enhanced in this section)
#fish type 1:
def fish1(x, y, scale, fill, body_color, tail_color):
    launch(x, y)
    t.right(30)

#body
    if fill:
        t.color(body_color)
        t.begin_fill()
        t.circle(60*scale, 60)
        launch(x, y)
        t.circle(-60*scale, 60)
        t.end_fill()

#tail
    if fill:
        t.color(tail_color)
        t.begin_fill()
        for i in range(3):
            t.forward(20*scale)
            t.left(120)
        t.end_fill()
        t.left(30)

#eye
    t.color("black")
    t.begin_fill()
    launch(x+10*scale, y-1*scale)
    t.circle(2*scale)
    t.end_fill()

#fish type-2

def fish2(x, y, scale, fill, body_color, tail_color):
    launch(x, y)

#body
    if fill:
        t.color(body_color)
        t.begin_fill()
        t.left(30)
        for i in range(3):
            t.forward(40*scale)
            t.right(120)
        t.end_fill()

    launch(x+20*math.sqrt(3)*scale, y)

#tail
    if fill:
        t.color(tail_color)
        t.begin_fill()
        for i in range(3):
            t.forward(20*scale)
            t.right(120)
        t.end_fill()
        t.right(30)

#eye
    launch(x+10*scale, y-1*scale)
    t.color("black")
    t.begin_fill()
    t.circle(2*scale)
    t.end_fill()



#draw the third type of fish called manta fish

def manta(x, y, scale, fill, color):

#draw a pentagon body and tale
    launch(x,y)
    if fill:
        t.color(color)
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
    for i in range(2):
        starting_x =[x-20*math.sqrt(3)*scale, x-5*math.sqrt(3)*scale]
        t.color("black")
        launch(starting_x[i], y-10*scale)
        t.begin_fill()
        t.circle(2*scale)
        t.end_fill()

    #mouth
    launch(x-17.5*math.sqrt(3)*scale, y-20*scale)
    t.forward(10*math.sqrt(3)*scale)



#define a scene about three different type of fishes standing on the rostrum of the Olympic
def scene1(x, y, scale):

    #draw the rostrum at a appropriate size, and olympic rings for decoration. Three types of fish were added too.
    rostrum(x, y, 100, scale, True, "grey")
    oly_ring(x+130*scale, y+30*scale, 0.2*scale)
    fish1(x+10*scale, y+60*scale, scale, True, "pink", "cyan")
    fish2(x+120*scale, y+140*scale, scale, True, "orange", "violet")
    manta(x+280*scale, y+90*scale, scale, True, "silver")


#define a new scene that contains scene1, fireworks and trees to make it surreal

#scenes within scenes within scenes within scenes
def scene2(x, y, scale, fill, fireworks_number, sys):
    #add scene1, three fishes in the Olympic rostrum, to the new scene
    scene1(x, y, scale)
    
    #add two trees to the scene
    for i in range(2):
        list_treex= [x-200*scale, x+400*scale]
        tree(list_treex[i], y, scale, sys)
    

    #add fireworks to the scene
    for i in range(fireworks_number): #firework_number is the initial number of fireworks would be add into the scene
        random_length=random.random() 
        if random_length>0.5: #The firework will be drawn only the random length factor greater than 0.5
            if fill:
                fireworks_color= (random.random(), random.random(), random.random()) #the color was randomly set
                fireworks(x+scale*random.randint(-400, 400),  
                y+scale*random.randint(200, 400), #random package also distribute the position of firework randomly
                random.randint(3, 10),  #the side of each firework is between 3 to 9
                30*random_length, scale, 
                True, fireworks_color, 
                scale*random.randint(5, 10)) #pensize of each firework was between 5 to 9


#In order to finish the taskC better, I revise the scene2 a little to get the new scene2_2 func.

def scene2_2(x, y, scale, fill, fireworks_color, sys): #add the list: fireworks_color to the parameter 
    
    scene1(x, y, scale)   #scene1 is the same
    
    #Trees are the same
    for i in range(2):
        list_treex= [x-200*scale, x+400*scale]
        tree(list_treex[i], scale, sys)
    

    #add fireworks to the scene with something new, the random package will not be used in this func
    for i in range(len(fireworks_color)): #analyze elements in the list
        if i > 0: #skip the first element in the list bcs the first element of list dont hold message
            if fill:
                fireworks(x+scale*random.randint(-400, 400),  
                y+scale*random.randint(200, 400), #random package also distribute the position of firework randomly
                random.randint(3, 10),  #the side of each firework is between 3 to 9
                30*random.random(), scale, 
                True, fireworks_color[i], 
                scale*random.randint(5, 10)) #pensize of each firework was between 5 to 9


if __name__ == "__main__":
    t.tracer(False)
    scene2(-100, -100, 1, True, 40, sys.argv)
    t.update()
    t.mainloop()