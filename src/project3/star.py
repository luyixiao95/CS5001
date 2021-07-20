#Luyi Xiao 
#CS 5001, Project 3
# 4th Feb, 2021

import turtle, sys

def star( rays, size ):
    print('Drawing a star with', rays, 'rays of size', size )

    # loop for the number of rays
    for i in range(rays):
        turtle.setheading( i * 360 / rays )
        turtle.forward( size )
        turtle.backward( size )

# top level code, make drawing fast
turtle.tracer(False)

# assign values to variables
numrays = 10
raysize = 50

# call the star function
star(int(sys.argv[1]), int(sys.argv[2]))

# update and hold open the window
turtle.update()
turtle.mainloop()