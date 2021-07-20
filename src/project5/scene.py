#Luyi Xiao 
#CS 5001 & 5003
#March 1st, 2021

#define a main function to draw the animate scene
#https://drive.google.com/file/d/1jTj6Wc72f4d8nLp3k7HHSGn4hcZrdzG_/view?usp=sharing
import time
import complex_objects as cob
import graphicsPlus as gr
import sys

def main(t): #t is the time delay of every frame
    win = gr.GraphWin("seasons", 750, 500)
    #use a list to conclude all the primary objects in the scene
    shapes_lists = [cob.newvol_init(100, 850, 3), cob.train_init(0, 450, 1.5), cob.tree_init(200, 500, 1.5),
    cob.meadow_init(240, 500, 1.5), cob.house_init(100, 500, 2),cob.rail_init(0, 450, 1.5), cob.cloud_init(200, 350, 1.5)
    ]

    shapes = []   #create a blank list to append the shapes object later
    for item in shapes_lists:  #Use for loop to draw graph from the shapes_list
        cob.draw(item, win)  #use the draw function in the complex_object package
        shapes.append(item)  #append the object to the new list

    for frame in range(100):    #use for loop to draw the scene from every frame from 0 to 00
        if win.checkMouse():  
            break               #break when click the mouse
        elif win.checkKey == "q":    #break when type "q"
            break
        else:      #use four functions in the cob package to animate the scene
            cob.animate_train(shapes[1], frame, win)
            cob.animate_tree(shapes[2], frame, win)
            cob.animate_meadow(shapes[3], frame, win)
            cob.animate_cloud(shapes[6], frame, win)
            time.sleep(t)
            win.update()

    win.getMouse()
    win.close()

print(sys.argv)  #use command line to input the time delay, please type in a float number

if __name__ == "__main__":

    #execute the main function with inputting a float number as the time delay
    main(float(sys.argv[1]))

