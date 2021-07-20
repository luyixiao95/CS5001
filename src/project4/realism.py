#Luyi Xiao
#CS 5001 & 5003
#Feb 16, 2021, realism.py

import complex_shapes as cxshape, graphicsPlus as gr, sys

#define a main function that can draw a combined graph with the objects in the complex_shapes.py
def main(x, y, scale):
    win = gr.GraphWin("Scene", 600, 600)
    
    #using "+" to combine three lists of shapes to a new list
    scene = cxshape.volcano_init(x, y, scale*0.5)+cxshape.island_init(x, y, scale*0.5) + cxshape.LaEra_init(x+50*scale, y+150*scale, scale)
    
    cxshape.draw(scene, win)
    win.getMouse()
    win.close()

#use the command line to input the x, y position and scale of the main function=
print(sys.argv)
if __name__ == "__main__":
    if len(sys.argv)>3: #test if the list in the command line has enough elemtns to the main() function
        main(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])) #use float() function to transfer the type of the elements
    else:
        print("The data in the command line are not enough. type more data again please")

