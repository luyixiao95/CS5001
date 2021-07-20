#Luyi Xiao
#CS 5001 & 5003
#Project 6: memes

import sys
import graphicsPlus as gr


#use command line to import the main function that can convey the picture
def main(command_list):
    if len(command_list) < 2:
        print("You need to import more information of the picture")
        exit()
    
    #read image data
    file=command_list[1]
    image = gr.Image(gr.Point(0, 0), file)
    width = image.getWidth()
    height = image.getHeight()
    win = gr.GraphWin(file, width, height)
    image.move(width/2, height/2)
    image.draw(win)
    win.getMouse()
    win.close()
    return image

if __name__ == "__main__":
    main(sys.argv)




