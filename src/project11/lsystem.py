#Luyi Xiao
#26 March, 2021
#CS5001 & CS5003
#lsystem.py version 4

#Revised in 2 April

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
        """ Replace all characters in the istring with strings from the
            right-hand side of the appropriate rule. This version handles
            parameterized rules.
        """
        tstring = ''
        parstring = ''
        parval = None
        pargrab = False

        for c in istring:
            if c == '(':
                # put us into number-parsing-mode
                pargrab = True
                parstring = ''
                continue
            # elif the character is )
            elif c == ')':
                # put us out of number-parsing-mode
                pargrab = False
                parval = float(parstring)
                continue
            # elif we are in number-parsing-mode
            elif pargrab:
                # add this character to the number string
                parstring += c
                continue

            if parval != None:
                key = '(x)' + c
                if key in self.rules:
                    replacement = random.choice(self.rules[key])
                    tstring += self.substitute( replacement, parval )
                else:
                    if c in self.rules:
                        replacement = random.choice(self.rules[c])
                        tstring += self.insertmod( replacement, parstring, c )
                    else:
                        tstring += '(' + parstring + ')' + c
                parval = None
            else:
                if c in self.rules:
                    tstring += random.choice(self.rules[c])
                else:
                    tstring += c

        return tstring
					    
    def substitute(self, sequence, value ):
        """ given: a sequence of parameterized symbols using expressions
            of the variable x and a value for x
            substitute the value for x and evaluate the expressions
        """

        expr = ''
        exprgrab = False

        outsequence = ''

        for c in sequence:

            # parameter expression starts
            if c == '(':
                # set the state variable to True (grabbing the expression)
                exprgrab = True
                expr = ''
                continue

            # parameter expression ends
            elif c == ')':
                exprgrab = False
                # create a function out of the expression
                lambdafunc = eval( 'lambda x: ' + expr )
                # execute the function and put the result in a (string)
                newpar = '(' + str( lambdafunc( value ) ) + ')'
                outsequence += newpar

            # grabbing an expression
            elif exprgrab:
                expr += c

            # not grabbing an expression and not a parenthesis
            else:
                outsequence += c 

        return outsequence

    def insertmod(self, sequence, modstring, symbol):
        """ given: a sequence, a parameter string, a symbol 
            inserts the parameter, with parentheses, 
            before each
            instance of the symbol in the sequence
        """
        tstring = ''
        for c in sequence:
            if c == symbol:
                # add the parameter string in parentheses
                tstring += '(' + modstring + ')'
            tstring += c
        return tstring
        
    #iterate the base with rules for given times
    def buildString(self, iteration):
        nstring = self.base

        for i in range(iteration):
            nstring = self.replace(nstring)
        
        return nstring
 
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


