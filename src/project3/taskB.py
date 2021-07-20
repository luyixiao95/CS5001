#Luyi Xiao
#CS 5001, project 3, taskB.py
#8th, Feb, 2021

import newshapelib as nslib, turtle as t, random

#draw picture 2 by calling the scene2 function in newshapelib

#The starting position of the function is (-100, -100), the scale is 1, fill the firework color 
#and the initial number of the fireworks is 40

t.tracer(False)
nslib.scene2(-100, -100, 1, True, 40)
t.update()
t.mainloop()
