# Timed mode main Function

from graphics import *
from actions import *
from scene import *
import time


def runTimeMode(win, blockcolor):

    amount = 999
    start = createStartBB(win)

    timeAlert = Text(Point(2, 0.25), 'You have 15 Seconds!')
    timeAlert.setSize(17)
    timeAlert.setStyle('bold')
    timeAlert.draw(win)

    bbGroup, locateGroup = createBB(win, amount, blockcolor)  
    timeini = firstClick(win, locateGroup)

    start[0].setFill('gray')
    start[1].undraw()
    start[0].undraw()
    start[0].draw(win)
    
    bbAllDown(bbGroup)   
    amount = amount - 1

    timePassed = 0

    while timePassed < 15:
        x1, x2, y1, y2 = firstBB(locateGroup)
        mouse_current = win.getMouse()
        mouseX = mouse_current.getX()
        mouseY = mouse_current.getY()

        time_current = time.time()
        timePassed = time_current - timeini

        if mouseX >= x1 and mouseX <= x2 and mouseY >= y1 and mouseY <= y2:
            print('good')
            bbAllDown(bbGroup)
            pass

        else:
            score = 998 - len(locateGroup)
            for i in range(amount):
                bbGroup[i].undraw()
            return score

    score = 999 - len(locateGroup)
    for i in range(amount):
        bbGroup[i].undraw()
    return score
