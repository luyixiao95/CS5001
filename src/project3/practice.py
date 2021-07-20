# list definitions

Vin = [ 'Vin', 'Scruffy', 'Mistborn' ]

Kelsier = [ 'Kelsier', 'Leader', 'Mistborn' ]

 

print( Vin[0] + " and " + Kelsier[0] + " travel through the mists" )

 

Sazed = [ 'Terris', 'Keeper', 'Sazed']

carriage = [Sazed]

 

carriage.append( Vin )

carriage.append( Kelsier )

 

print( carriage[0][2] + " meets the two " + carriage[-1][-1] + " on the road to Fellise")

 

Renoux = [ 'Lord Renoux', 'Noble', 'Kandra' ]

 

mansion = [ Renoux, carriage.pop(), carriage.pop(), carriage.pop() ]

 

Vin[1] = 'Elegant'

Vin.append( 'Formal Dress' )

 

print( Vin[0] + " gets a haircut and a " + mansion[2][-1] )