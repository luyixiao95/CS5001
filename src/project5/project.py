#Luyi Xiao
#CS5001 & 5003
#Project 5 animation

import time 
import random
import graphicsPlus as gr


#define objects

def init_saucer(x, y, scale):
    light = gr.Circle(gr.Point(x, y-20*scale), 4*scale)
    light.setFill(gr.color_rgb(220, 100, 110))
    body = gr.Oval(gr.Point(x-30*scale, y-20*scale), gr.Point(x+30*scale, y+20*scale))
    body.setFill(gr.color_rgb(220, 210, 220))
    saucer = gr.Oval(gr.Point(x-60*scale, y-5*scale), gr.Point(x+60*scale, y+5*scale))
    saucer.setFill(gr.color_rgb(240, 230, 190))
    saucer_list=[light, body, saucer]
    return saucer_list



def draw( shapes, win ):
    """ Draw all of the objects in shapes in the window (win) """
    for item in shapes:
        item.draw(win)
def move( shapes, dx, dy ):
    """ Draw all of the objects in shapes by dx in the x-direction
    and dy in the y-direction """
    for item in shapes:
        item.move(dx, dy)
def undraw( shapes ):
    """ Undraw all of the objects in shapes """
    for item in shapes:
        item.undraw()


def animate_saucer(shapes, frame_num, win ):
    if frame_num == 70:
        mid = shapes[0].getCenter()
        radius = shapes[0].getRadius()
        scale = radius/4
        beam = gr.Polygon(gr.Point(mid.getX()-scale*4, mid.getY()+scale*40), 
        gr.Point(mid.getX() + scale*4, mid.getY() + scale*40), gr.Point(mid.getX() + scale*15, mid.getY() + scale*110), 
        gr.Point(mid.getX() - scale*15, mid.getY() + scale*110))
        beam.setFill(gr.color_rgb(255, 255, 180))
        beam.draw(win)
        shapes.append(beam)

    if frame_num == 90:
        beam = shapes.pop()
        beam.undraw()

    
    if frame_num < 25:
        move(shapes, 0, -3)
    elif frame_num >= 25 and frame_num< 50:
        move(shapes, 0, 3)
    elif frame_num >= 50 and frame_num< 75:
        move(shapes, -3, 0)
    else:
        move(shapes, 3, 0)

    
    if frame_num %20 == 0:
        shapes[0].setFill("blue")
    elif frame_num % 20 == 10:
        shapes[0].setFill("red")





def main():
    win = gr.GraphWin("saucer", 400, 400, False)
    
    saucer = init_saucer(200, 200, 2)
    draw(saucer, win)
    for frame in range(100):

        if win.checkMouse() :
            break

        elif win.checkKey() == "q":
            break

        else:
            animate_saucer(saucer, frame, win)
            time.sleep(0.1)
            win.update()
    win.update()
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()