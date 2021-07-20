class Person():

    def __init__(self, name, kind):

        self.name = name

        self.kind = kind

 

    def getName(self):

        return self.name

 

    def getKind( self ):

        return self.kind

 

class Ska(Person):

    def __init__(self, name, status):

        Person.__init__(self, name, 'Ska')

        self.status = status

 

    def getStatus(self):

        return self.status

 

    def setStatus(self, status):

        self.status = status

 

class Koloss(Person):

    def __init__(self, state):

        Person.__init__(self, 'me', 'Koloss')

        self.state = state

 

    def setState(self, state):

        self.state = state

 

def wellOfAscension():

 

    vin = Ska( 'Vin', 'mistborn' )

    penrod = Ska( 'Ferson Penrod', 'king' )

    straff = Ska( 'Straff Venture', 'lord' )

    cett = Ska( 'Cett', 'lord' )

    eland = Ska( 'Eland Venture', 'citizen' )

    koloss = []

    for i in range( 10000 ):

        koloss.append( Koloss( 'docile' ) )

 

    print( straff.getName() + " pulls his army away from Luthadel" )

    for creature in koloss:

        creature.setState( 'bloodrage' )

    print( 'The Koloss take over Luthadel' )

    print( vin.getName() + " returns and takes control of the Koloss")

    for creature in koloss:

        creature.setState( 'obedient' )

    straff.setStatus( 'deceased' )

    eland.setStatus( 'emperor' )

 

    print( vin.getName() + " and " + eland.getName() + " go to the well" )

    print( vin.getName() + " releases Ruin " )

    eland.setStatus( eland.getStatus() + ' and mistborn' )

    # mark 1                                                                                                  

 

if __name__ == "__main__":

    wellOfAscension()