#Luyi Xiao
#CS 5001 & CS 5003
#Final, creating a small game using graphics.py

import graphicsPlus as gr
import random

win = gr.GraphWin("win", 400, 800)
block_list = []


def block(col, row=0):
    #make sure x < 10
    if col>=10:
        print("Starting point fault")
        return
    if len(block_list) > 3:
        win.update()
        win.getMouse()
        win.close()
        return None

    if (col, row) not in block_list:
        block_list.append((col, row))
    print(block_list)
    xpo = col * 40
    ypo = row * 40

    base = gr.Rectangle(gr.Point(xpo, ypo), gr.Point(xpo+40, ypo+40))
    base.draw(win)
    dice = random.random()
    if dice < 0.3 and col - 1 > 0:
        col = col - 1

    elif dice >= 0.3 and dice < 0.6 and row - 1 > 0:
        row = row - 1

    elif dice >= 0.6 and dice <0.8:
        col = col + 1

    elif dice >=0.8:
        row = row + 1

    block(i+1, col, row)
    return 

   

    


block(1, 3, 0)
