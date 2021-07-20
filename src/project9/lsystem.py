#LUyi Xiao
#26 March, 2021
#CS5001 & CS5003
#lsystem.py version 3

import sys
import random

#define a class Lsystem
class Lsystem:

    def __init__(self, filename = None):
        self.base = ''
        self.rules = {}
        if filename != None:
            self.read(filename)
    
    #return the base of the Lsystem class
    def getBase(self):
        return self.base
    
    #mutate the base of the Lsystem class
    def setBase(self, b):
        self.base = b
    
    #return the rule
    def getRule(self, index):
        return self.rule[index]
    
    #mutate the rule 
    def addRule(self, newrule):
        self.rules[newrule[0]]=newrule[1:]

    def numRules(self):
        return len(self.rule)

    #rearrange the base and rule from the file
    def read(self, filename):
        self.rule = []
        fp = open(filename, "r")
        lines = fp.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(' ')
            if line[0] == "base":
                self.setBase(line[1])
            elif line[0] =="rule":
                self.addRule(line[1:])
        
        fp.close()

    #replace the string with the rule
    def replace(self, istring):
  # assign to a local variable (e.g. tstring) the empty string
        tstring = ""
        for c in istring:
            if c in self.rules:
                tstring += random.choice(self.rules[c])
            else:
                tstring += c

        return tstring        
        
    #iterate the base with rules for given times
    def buildString(self, iteration):
        nstring = self.base

        for i in range(iteration):
            nstring = self.replace(nstring)
        
        return nstring
    #cast the class to a string
    """
    def __str__(self):
        string = "base X\nrule X -> F-[[X]+X]+F[+FX]-X\nrule F -> FF"
        return string"""

#define a main function                
def main(argv):
    lsys = Lsystem()
    iterations = 2


    if len(argv) >= 2:
        filename = argv[1]
        lsys.read( filename )
    
    else:
        lines = str(lsys)
        newlines = lines.replace(" ->", "")
        newlines = newlines.split("\n")
        for line in newlines:
            line = line.split(" ")
            if line[0] == "base":
                lsys.setBase(line[1])
            if line[0] == "rule":
                lsys.addRule(line[1:])            


    print( lsys )

    for i in range( lsys.numRules() ):
      rule = lsys.getRule(i)
      print( rule[0] + ' -> ' + rule[1] )

    lstr = lsys.buildString( iterations )
    print( lstr )

    return lstr

if __name__ == "__main__":
    main(sys.argv)


