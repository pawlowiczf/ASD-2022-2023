from egz3btesty import runtests

def uncool( P ):
    #
    for a in range( len(P) ):
        x, y = P[a]
        P[a] = [x, y, a]
    #

    P.sort()
    pointer = 0 

    a = 0
    for i in range(1, len(P)):
        while(a<i and P[a][1]<P[i][0]): a+=1
        if P[a][0]<P[i][0] and P[a][1]<P[i][1]: return (P[a][2], P[i][2])
    #

#end procedure uncoll()           


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )


