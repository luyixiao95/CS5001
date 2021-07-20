#Luyi Xiao
#CS 5001 & 5003
#Project 6: memes
import graphicsPlus as gr
import sys
import show

#define a function to switch the red and blue color of the pixel
def swapRedBlue(src):
    rows = src.getHeight()
    cols = src.getWidth()

    for row in range(rows):
        for col in range(cols):
            r, g, b = src.getPixel(col, row)

            src.setPixel(col, row, gr.color_rgb(b, g , r))


#define a negitive filter that all r, g, b colors are the opposite the original ones
def Negitive(src):
    rows = src.getHeight()
    cols = src.getWidth()

    for row in range(rows):
        for col in range(cols):
            r, g, b = src.getPixel(col, row)

            src.setPixel(col, row, gr.color_rgb(255-r, 255-g, 255-b))


#define a gray filter that the original picture is shown in the grayscale
def Gray(src):
    rows = src.getHeight()
    cols = src.getWidth()

    for row in range(rows):
        for col in range(cols):
            r, g, b = src.getPixel(col, row)

            gray = (r+g+b)//3

            src.setPixel(col, row, gr.color_rgb(gray, gray, gray))

#Define a enhance function to make color in a more contrast way
def Enhance(src):
    rows = src.getHeight()
    cols = src.getWidth()

    for row in range(rows):
        for col in range(cols):
            r, g, b = src.getPixel(col, row)
            color_list = [r, g, b]
            new_color_list=[]
            for color in color_list:
                if color < 128:
                    color = int(color * 0.75)
                elif color >=128:
                    color = int(color*1.25)
                    color = min(color, 255)   
                new_color_list.append(color)
            src.setPixel(col, row, gr.color_rgb(new_color_list[0], new_color_list[1], new_color_list[2]))  

#Define a sepia function to create a sepia filter  
def Sepia(src):
    rows = src.getHeight()
    cols = src.getWidth()

    for row in range(rows):
        for col in range(cols):
            r, g, b = src.getPixel(col, row)
            newr = min(int(0.393*r + 0.769*g + 0.189*b), 255)
            newg = min(int(0.349*r + 0.686*g + 0.168*b), 255)
            newb = min(int(0.272*r + 0.534*g + 0.131*b), 255)
            src.setPixel(col, row, gr.color_rgb(newr, newg, newb))

#define a cartoon function to make a sketch function
def Cartoon(src):
    rows = src.getHeight()
    cols = src.getWidth()

    for row in range(rows):
        for col in range(cols):
            r, g, b = src.getPixel(col, row)
            color_list = [r, g, b]
            new_color_list= []
            for color in color_list:
                color = color // 32
                color = color*32
                new_color_list.append(color)
            src.setPixel(col, row, gr.color_rgb(new_color_list[0], new_color_list[1], new_color_list[2]))


#define a blur function that the color of a pixel is the average color of the 8 nearest pixels
def Blur(src):
    rows = src.getHeight()
    cols = src.getWidth()
    clone = src.clone()
    for row in range(rows):
        for col in range(cols):
            if row != 0 and col != 0 and row != rows-1 and col != cols-1:
                rc00, gc00, bc00 = clone.getPixel(col-1, row-1)
                rc10, gc10, bc10 = clone.getPixel(col, row-1)
                rc20, gc20, bc20 = clone.getPixel(col+1, row-1)
                rc01, gc01, bc01 = clone.getPixel(col-1, row)
                rc11, gc11, bc11 = clone.getPixel(col, row)
                rc21, gc21, bc21 = clone.getPixel(col+1, row)
                rc02, gc02, bc02 = clone.getPixel(col-1, row+1)
                rc12, gc12, bc12 = clone.getPixel(col, row+1)
                rc22, gc22, bc22 = clone.getPixel(col+1, row+1)
                rs, gs, bs = src.getPixel(col, row)
                rs = int((rc01 + rc02 + rc10 + rc11 + rc12 + rc20 + rc21 + rc22)/8)
                gs = int((gc01 + gc02 + gc10 + gc11 + gc12 + gc20 + gc21 + gc22)/8)
                bs = int((bc01 + bc02 + bc10 + bc11 + bc12 + bc20 + bc21 + bc22)/8)
                src.setPixel(col, row, gr.color_rgb(rs, gs, bs))




#define a text function for the swapRedBlue function
def text():
    src = show.main(sys.argv)
    swapRedBlue(src)

if __name__ == "__main__":
    text()




