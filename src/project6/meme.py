#Luyi Xiao
#7, March, 2021
#CS 5001 & CS 5003 Project 6, Meme

import graphicsPlus as gr
import filter
import sys

#a list that contains the name of original pictures in the directory
originals = ["cat.ppm", "lazycat.ppm", "Dog.ppm", "worm.ppm", "flowers.ppm"]

#a list contains filter in the library
filters = ["swapRedBlue", "Negitive", "Gray", "Enhance", "Sepia", "Cartoon", "Blur"]

#define the first meme of a cat enjoying its coding 
def meme(src):
    if len(src)<3:      #At least contains three elements in the list
        print("You need to add more elements in the command line")
        return

    name = src[1]
    fil = src[2]

    if name not in originals:  #test the name in the directory
        print("You should type in the filename that is in the directory")

        return None

    image = gr.Image(gr.Point(0, 0), name)
    cols = image.getWidth()
    rows = image.getHeight()
    win = gr.GraphWin(name, cols, rows)
    image.move(cols/2, rows/2)

    if fil not in filters: #make sure that the filter typed in is in the library
        print("You need to type in the filter in the library")
        return

    else:
        if fil == filters[0]:
            filter.swapRedBlue(image)
        if fil == filters[1]:
            filter.Negitive(image)
        if fil == filters[2]:
            filter.Gray(image)
        if fil == filters[3]:
            filter.Enhance(image)
        if fil == filters[4]:
            filter.Sepia(image)
        if fil == filters[5]:
            filter.Cartoon(image)
        if fil == filters[6]:
            filter.Blur(image)

    image.draw(win)


    if len(src) >= 6:
        try:
            words = src[3]
            text_x = int(src[4])
            text_y = int(src[5])
            text = gr.Text(gr.Point(text_x, text_y), words)
            text.draw(win)
            if len(src) > 6:   #Add additional informations to the meme
                color = src[6] #color should be the 6th element in the command list
                size = int(src[7])  #size should be the 7th element
                text.setFill(color)
                text.setSize(size)

        except:
            print("Something went wrong with the color of size of the text")






   #why "filter.fil(image): cannot be in the program?

    return win


#define a test function for this meme function

def test(src):
    win = meme(src)
    if win:
        win.getMouse()
        win.close()

test(sys.argv)



