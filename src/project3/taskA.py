#Luyi Xiao
#CS 5001, project 3, taskA.py
#8th, Feb, 2021

import newshapelib as nslib, turtle as t, random

#Draw scene1 three times to bulid picture 1
t.tracer(False)

nslib.scene1(-300, -300, 1.3)
nslib.scene1(-80, -100, 1)
nslib.scene1(100, 100, 0.6)
t.update()
t.mainloop()
