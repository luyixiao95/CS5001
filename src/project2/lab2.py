#luyi xiao
#CS 5001 2021 Spring 
#Lab 2 code file
import turtle as t, random
#move turtle to location(x,y)
def goto(x,y):
    t.up()
    t.goto(x,y)
    t.down()

#draw a rectangle by looping

def rectangle(x , y , scale):
#starting point is (x,y)

    goto(x,y)
#looping for a rectangle with certain scales and specific height and width 
    for i in range(4):
        if i%2 == 0:
            t.forward(50* scale)
            t.right(90)
        else:
            t.forward(100* scale)
            t.right(90)

#house contains three blocks(rectangles)
def house(x, y, scale):
    rectangle(x , y, scale)
    rectangle(x+(50*scale)/4, y+100*scale/2, scale/2)
    rectangle(x+(50*scale)/4+(50*scale/8),y+100*scale/2+100*scale/4, scale/4)

t.tracer(False)

house(-100,-100,1.5)

def random_house(n):
    for i in range(n):
        house(random.randint(-50,50), random.randint(-50,50), random.random())
t.mainloop()