#Luyi Xiao
#CS 5001 & 5003
#Feb 12, 2021 (Happy Chinese New Year!)
#messing.py 

#using graphicsPlus to draw something

import graphicsPlus as gr

def init_rocket(x, y, scale):

    #body
    return [gr.Rectangle(gr.Point(x-scale*10, y), gr.Point(x+scale*10, y-scale*80)),
    gr.Polygon(gr.Point(x-scale*10, y-scale*80), gr.Point(x, y-scale*100), gr.Point(x+scale*10, y-scale*80)),
    gr.Polygon(gr.Point(x-scale*10, y), gr.Point(x-scale*10, y-scale*20), gr.Point(x- scale*25, y+scale*5)),
    gr.Polygon(gr.Point(x+scale*10, y), gr.Point(x+scale*10, y-scale*20), gr.Point(x+scale*25, y+scale*5))]
    

    # define the rocket shapes here and put them in a list
    

def main():
    # Create a GraphWin window that is at least 400 x 400
    win=gr.GraphWin("Rocket", 400, 400)


    # assign to rocket1 the result of calling init_rocket with arguments 100, 300, 1
    rocket1= init_rocket(100, 300, 1)

    # for each shape in rocket1
        # draw the shape into the window
        
    for shape in rocket1:
        shape.draw( win )
        shape.setFill("red")
    win.getMouse()
    win.close()

    # wait for a mouse click
    # close the window

if __name__ == "__main__":
    main()
