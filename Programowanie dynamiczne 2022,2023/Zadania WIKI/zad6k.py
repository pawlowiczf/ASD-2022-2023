from zad6ktesty import runtests 

"""
f(i) - ilosc mozliwych roznych zakodowanych wiadomosci
f(i) = f(i-1) + f(i-2)

if T[i-1] >= 3: f(i) = f(i-1)
if T[i-1] == 0: to T[i] musi byc z przedzialu <1, 9>
if T[i-1] == 1: to T[i] <0, 9>
if T[i-1] == 2: to T[i] <0, 6>

"""

def Possibilities( S ):
    #
    n = len(S)
    F = [ None for _ in range(n) ]

    if 1 <= int( S[0] ) <= 9:
        F[0] = 1
    else:
        F[0] = 0
    #


    def rek(i):
        #
        if i <= 2:
            return F[i]
        #

        if F[i] == None:

            if int( S[i-1] ) >= 3:
                F[i] = rek(i - 1)

            elif int( S[i-1] ) == 0 and 1 <= int( S[i] ) <= 9:
                F[i] = rek(i-1) + rek(i-2)
            
            elif int( S[i-1] ) == 1 and 0 <= int( S[i] ) <= 9:
                F[i] = rek(i-1) + rek(i-2)
            
            elif int( S[i-1] ) == 2 and 0 <= int( S[i] ) <= 6:
                F[i] = rek(i-1) + rek(i-2)

        #end 'if' clause 
        
        return F[i]  
    #end def 

    return rek(n - 1)
#end procedure Possibilities()



def haslo ( S ):
    return Possibilities(S)

runtests ( haslo )