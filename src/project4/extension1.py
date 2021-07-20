#Luyi Xiao
#CS 5001 & 5003
#Feb 16, 2021, extension1.py 
import math, random
import graphicsPlus as gr
import complex_shapes as cxshape



#define a main function.  Draw a scene which an island is suffering from a huge earthquake
def main():
    win=gr.GraphWin("island", 600, 600)
    scene = cxshape.island_init(100, 100, 1) #use the function in cxshape to draw an island
    cxshape.draw(scene, win)
    while True:
        key = win.checkKey()
        if key == "q" : #win click q button, break the while statement.
            break
        for item in scene:
            x=-1*random.random()+1*random.random() #let the elements in the list move a little bit randomly in x position
            y=-1*random.random()+1*random.random() #let the elements in the list move a little bit randomly in y position
            item.move(x , y)   #The island is shaking like an earthquake
        win.update()
    win.getMouse()
    win.close()

    


if __name__ == "__main__":
    main()

