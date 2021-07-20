#Luyi Xiao
#CS5001 2020 Spring, Lab2, extension1.py
#Feb 2 2021
#Draw a tree

from turtle import *

#Define a function to draw a tree using simple recursion
def tree(length):

    if length > 1:
        forward(length)
#right branch
        right(20)   
        tree(length-10)
#left branch
        left(40)
        tree(length-10)

        
        right(20)       
        up()
        backward(length)
        down()

tracer(False)
up()
goto(-0,-200)
down()
left(80)
tree(80)
update()
mainloop()