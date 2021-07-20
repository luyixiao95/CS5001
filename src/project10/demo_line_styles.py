#Luyi Xiao
#4st April, 2021
#CS5001 & CS5003
#demo_line_styles.py

import shapes
import turtle_interpreter

#main function create a scene contains "normal", "jitter", "jitter3", "dotted"
def main():
    squ = shapes.Square()
    squ.setStyle("normal")
    width_list = [2, 6]
    init_width = squ.width
    #Use for loop to draw two squares with different width
    for i in range(2):
        squ.setWidth(width_list[i])
        squ.draw(-200 + i*300, 300)

    squ.setWidth(init_width)
    #Use nested for loop to make the jitter and jitter3 styles more encapsulated 
    jitter_list = ["jitter", "jitter3"]
    init_jitterSigma = squ.jitterSigma
    for i in range(len(jitter_list)):
        squ.setStyle(jitter_list[i])
        sigma_list = [1, 10]
        for j in range(len(sigma_list)):
            squ.setJitter(sigma_list[j])
            squ.draw(-200 + j*300, 150-i*150)
            squ.setJitter(init_jitterSigma)

    #Use for loop to draw two shapes with dotted style and different dot sizes
    squ.style = "dotted"
    dot_list = [1, 10]
    init_dot = squ.dotSize
    for i in range(len(dot_list)):
        squ.setDotSize(dot_list[i])
        squ.draw(-200 + i*300, -150)
    squ.setDotSize(init_dot)



    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == "__main__":
    main()
