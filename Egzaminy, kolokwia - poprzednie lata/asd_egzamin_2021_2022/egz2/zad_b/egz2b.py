from egz2btesty import runtests

"""
Dynamik:
f(i, g) - ile zlota od tej komanty 
"""

def Rek(C, F, room, bars):
    #
    if room == len(C) - 1: 
        F[room] = bars 
        return bars 

    value = C[room][0]

    if F[room] == -float('inf'):

        for (K, W) in C[room][ 1 : ]:

            if W != -1:
                
                if value - bars <= K <= value:
                    F[room] = max( F[room], Rek(C, F, W, bars - (value - K ) ) )

                if value <= K <= value + bars: 
                    F[room] = max( F[room], Rek(C, F, W, bars - (bars + value - K) ) )



        #
    return F[room]
#end procedure Rek()


def magic( C ):
    #
    F = [ -float('inf') for _ in range( len(C) ) ]
    value = Rek(C, F, 0, 0)

    return value

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = False )
