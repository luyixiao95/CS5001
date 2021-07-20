#Luyi Xiao
#CS5001 2020 Spring, Lab2, scene2.py
#Feb 2 2021
#draw a scene of the sea with fish1(x0, y0, scale), fish2(x0, y0, scale), manta(x0, y0, scale)
import shapelib as slib, turtle as t, math, random

#This scene contains m fish1, n fish2 and p manta fish by random size and random places.
def scene2(m, n, p):
    for i in range(m):
        slib.fish1(random.randint(-300, 300), random.randint(-300, 300), random.uniform(0.5,2.5))
    
    for i in range(n):
        slib.fish2(random.randint(-300, 300), random.randint(-300, 300), random.uniform(0.5,2.5))

    for i in range(p):
        slib.manta(random.randint(-300, 300), random.randint(-300, 300), random.uniform(0.5,2.5))

t.tracer(False)
scene2(8, 5, 3)
t.update()
t.mainloop()


