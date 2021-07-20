#Luyi Xiao
#CS5001 2020 Spring, Lab2, extension2.py
#Feb 2 2021
#draw a N-gon with distance with two parameters-distance and side

import turtle as t
def n_gon(distance, side):
    for i in range(side):
        t.forward(distance)
        t.left(360/side)

t.tracer(False)


n_gon(60, 6)
t.update()
t.mainloop()