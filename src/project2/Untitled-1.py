def pewter( strength ):

    return strength + 5

 

def tin( senses ):

    return senses + 6

 

def flare( power ):

    flaredpower = power * 10

    # mark 1                                                                    

    return flaredpower

 

Ham = "pewterarm"

Spook = "tineye"

Vin = "mistborn"

vstrength = 1

vsenses = 3

 

for i in range(4):

    if i < 2:

        print("Vin trains with Ham")

        vpower = pewter( vstrength )

    else:

        print("Vin trains with Spook")

        vpower = tin( vsenses )

 

    if i % 2 == 1:

        print("Vin tries to flare her metal", print(flarepower)) # mark 2