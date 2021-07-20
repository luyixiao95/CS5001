#Luyi Xiao
#CS 5001, project 3, taskC.py
#8th, Feb, 2021

import newshapelib as nslib, turtle as t, random, sys

#Using sys.argv: the command-line argument
print(sys.argv)

#the command-line argument input the color of the fireworks
list_of_color=sys.argv
t.tracer(False)

#change the nslib.scene2 a little bit to nslib.scene2_2
nslib.scene2_2(-100, -100, 1, True, list_of_color)
t.update()
t.mainloop()