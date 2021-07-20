#Luyi Xiao
#CS 5003 Project 1, extensions.py, 
#Jan 27, 2021

#N-gon
from turtle import *
#define a function that can draw a n-gon with two parameter, n and size. 
#n represents the n-gon's sides.
#size represents the size of every side.
def n_gon(n, size):
    i=0
    while i< n:
        forward(size)
        right(360/n)
        i = i+1

n_gon(7,50)
mainloop()