#This is a list of sublists each containing two items: a person's name, list of their abilities (only one ability for now)
population = [  
        ['Wax', ['Coinshot'] ] ,  
	['Marasi', [ 'Pulser'] ]  , 
	['Wayne', ['Slider'] ] 
	]


# Q1 - Turn the list into a dictionary (eg. abilities) where each sublist item translates into a key:value pair
# [name, [abilities...] ] translates to {name : [abilities...]} 
abilities = {}
for sublist in population:
    abilities.update({sublist[0]:sublist[1]})


# this creates a new entry in the dictionary since there is no Steris key
abilities.update({'Steris': ['TBD']})
# these update (replace) the value for the existing keys "Wax" and "Marasi" respectively
abilities.update({'Wax': ['Coinshot', 'Skimmer']})
abilities.update({'Marasi': ['Pulser']})


# Q2 - Update Wayne's abilities to : ['Slider', 'Bleeder']

abilities.update("Wayne" : ["Slider", "Bleeder"])
# Q3 - Write two expressions that print Marasi's list of abilities, one using the list population and the other using abilities dictionary
# Do not assume you know the index for Marai's sublist.
# What would be the runtime of each? (linear or constant time) Is one faster? Why?


# Q4 - Display the population's list of abilities: Traverse the dictionary keys and store the values of the abilities
# in a list called vals. Print each person with their list of abilities ("Marasi's abilities include: ..."). 
# Lastly, print the resulting vals list.


# Q5 - Fill in the incomplete method definitions of the Person class below

class Person:
    def __init__(self, name, abilities, profession = None):
        self.name = name
        self.abilities = abilities

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getAbilities(self):
        return self.abilities

    def setName(self, n):
        self.name = n

    def setAge(self, newAge):
        self.age = newAge

    # q - create a method to add to a Person's list of abilities
    def addAbility(self, a):
        pass

    # q - create a method to add a Person's profession 
    def createProfession(self, p):
        pass

    # q - create method to determine if Person has specified ability ab
    def hasAbility(self, ab):
        pass

    def printAbilities(self):
        for i in self.abilities:
            print(i)


#Below are three Person objects, the abilities list fields are assigned by accessing the abilities dictionary
#If the key specified in the call to the dictionary's get method does not exist an empty list is given
#to initialize the Person object 
wayne = Person('Wayne', abilities.get('Wayne'),[])
marasi = Person('Marasi', abilities.get('Marasi'), [])
steris = Person('Steris', abilities.get('Steris'), [])


# Q6 - create a Person object (eg. wax), once object is created use your methods to: 
# 1) update Wax's profession to 'Lawman,'
wax = Person('Wax', abilities.get('Wax'), [])
wax.createProfession('Lawman')


#Call the test function with a list of your Person objects as argument, it should print out who has Coinshot ability and who does not
def test(ppl):
    for p in ppl:
        if p.hasAbility('Coinshot'):
            print('%s is the Coinshot' % p.name)
        elif not p.hasAbility('Coinshot'):
            print('%s is not a Coinshot but a ' % p.name, end = "")
            p.printAbilities()


#if __name__ == "__main__": uncomment and call test function