#Luyi Xiao
#CS5001 & CS5003
#22 March, 2021
#Extension1.py
import turtle_interpreter
import lsystem


lsys = lsystem.Lsystem()
lines = str(lsys)
def extension():
    #delete the arrow symbol from the class string
    newlines = lines.replace(" ->", "")
    #split different lines as different elements in a list
    newlines = newlines.split("\n")

    for line in newlines:
        #split every word in every line as elements in certain list
        line = line.split(" ")
        #mutate the base and rules of the class
        if line[0] == "base":
            lsys.setBase(line[1])
        if line[0] == "rule":
            lsys.addRule(line[1:]) 
    #iterate 4 times
    lstr = lsys.buildString(4)  

    ti = turtle_interpreter.TurtleInterpreter()
    ti.place(0, -100, 90)
    ti.setColor("brown")
    ti.setWidth(4)
    ti.drawString(lstr, 10, 20)
    ti.place(0, -200)
    ti.write(lsys)
    ti.hold()

if __name__ == "__main__":
    extension()