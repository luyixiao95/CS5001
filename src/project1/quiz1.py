def decoding( first, second, third ):

    combined = third + first + second

    return combined

 

 

contract = 1000

payment = 1000

boxings = decoding( contract, contract, payment )

groupOfTheives = "crew "

 

Vin = decoding( "street ", "urchin", "gifted " )

Kelsier = decoding( "leader ", "and mistborn", groupOfTheives )

Camon = decoding( groupOfTheives, "leader", "cruel " )

Dockson = decoding( "con ", "artist", "high class " )

 

print("Vin, the " + Vin + ", helps Camon, a " + Camon + ", steal " + str(boxings) + " boxings")

print("Kelsier, a " + Kelsier + ", and Dox, a " + Dockson + ", save Vin" )