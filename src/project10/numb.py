import numpy as np 
from matplotlib import pyplot as plt 
 
x = [1, 2, 4, 8, 16]
y1 = [1, 2, 4, 8, 16]
y2 = [1, 2, 4, 8, 16]
y3 = [0, 1, 2, 3, 4]
plt.title("Graphing Search Algorithms") 
plt.xlabel("List of Length") 
plt.ylabel("Number") 
plt.scatter(x , y1)
plt.plot(x, y1, label = "ordered linear search" )
plt.scatter(x, y2)
plt.plot(x, y2, label = "chunk search", linestyle = "--" )
plt.scatter(x, y3)
plt.plot(x, y3, label = "binary search", linestyle = ":")
plt.legend(loc = "upper left")
plt.show()