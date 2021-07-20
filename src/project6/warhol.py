#Luyi Xiao
#CS 5001 & 5003
#Project 6: memes

import sys
import graphicsPlus as gr
import filter 

#define a function that contains 4-panel, with 4 pictures under certain filters
def warhol(command_list):
    filename = command_list[1]
    effects = command_list[2:]
    origin = gr.Image(gr.Point(0, 0), filename)
    cols = origin.getWidth()
    rows = origin.getHeight()
    panel = len(effects)
    win = gr.GraphWin(filename, cols*panel, rows)
    origin.move(cols/2, rows/2)

    for i in range(panel):
        clone = origin.clone()
        if effects[i] == "swapRedBlue":
            filter.swapRedBlue(clone)
        elif effects[i] == "Enhance":
            filter.Enhance(clone)
        elif effects[i] == "Sepia" :
            filter.Sepia(clone)
        elif effects[i] == "Cartoon":
            filter.Cartoon(clone)
        elif effects[i] == "Gray":
            filter.Gray(clone)

        clone.move(cols*i, 0)
        clone.draw(win)
    
    return win

#define a main function to draw three pictures with different filters
def main():
    if len(sys.argv) < 3:
        print("You need to input at least one filter")
        return
    
    win = warhol(sys.argv)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()




