# create black block and win check

from random import randint
from graphics import *
import time

def createBB(win, amount, color):
    bbGroup = []
    locateGroup = []
    
    for i in range(amount):
        location = randint(0, 3)
        bb = Rectangle(Point(location, i + 1), Point(location + 1, i + 2))
        bb.setFill(color)
        bb.draw(win)

        bbGroup.append(bb)
        locateGroup.append(location)

    return bbGroup, locateGroup

def createEndBB(win, bbGroup, amount):
    end = Rectangle(Point(0, amount + 1), Point(4, amount + 4))
    end.setFill('green')
    end.draw(win)
    bbGroup.append(end)

    end_Text = Text(Point(2, amount + 1.5), 'END!')
    end_Text.setSize(20)
    end_Text.setStyle('bold')
    end_Text.draw(win)
    bbGroup.append(end_Text)

    return bbGroup

def createStartBB(win):
    start = Rectangle(Point(0, 0), Point(4, 1))
    start.setFill('red')
    start.draw(win)

    start_text = Text(Point(2, 0.5), 'Click on first black block to start!')
    start_text.setSize(17)
    start_text.setStyle('bold')
    start_text.draw(win)

    sbb = []
    sbb.append(start)
    sbb.append(start_text)

    return sbb

def firstBB(locateGroup):
    firstlocate = locateGroup.pop(0)
    x1 = firstlocate
    x2 = firstlocate + 1
    y1 = 1
    y2 = 2

    return x1, x2, y1, y2
    

def bbAllDown(bbGroup):
    for i in range(len(bbGroup)):
        bbGroup[i].move(0, -1)
        
def firstClick(win, locateGroup):
    mouseX = 0
    mouseY = 0
    x1, x2, y1, y2 = firstBB(locateGroup)

    while mouseX < x1 or mouseX > x2 or mouseY < y1 or mouseY > y2:
        mouse_current = win.getMouse()
        mouseX = mouse_current.getX()
        mouseY = mouse_current.getY()

    timeini = time.time()
    print('good')
    return timeini

def run_game(win, bbGroup, locateGroup):
    for i in range(len(locateGroup)):
        x1, x2, y1, y2 = firstBB(locateGroup)
        mouse_current = win.getMouse()
        mouseX = mouse_current.getX()
        mouseY = mouse_current.getY()

        if mouseX >= x1 and mouseX <= x2 and mouseY >= y1 and mouseY <= y2:
            print('good')
            bbAllDown(bbGroup)
            pass

        else:
            gameEnd = True
            return gameEnd

    gameEnd = False
    return gameEnd
            


















