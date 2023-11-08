def countingSort(A, p, way):
    B = [0] * len(A)
    C = [0] * 10
    #
    for i in range( len(A) ):
        C[ A[i][p] ] += 1
    #
    if way == 1:
        for i in range( 1, len(C) ):
            C[i] += C[i-1]
    else:
        for i in range( len(C) - 2, -1, -1):
            C[i] += C[i+1]
    #
    for i in range( len(A) - 1, -1, -1 ):
        B[ C[ A[i][p] ] - 1 ] = A[i]
        C[ A[i][p] ] -= 1
    #
    return B
#end def ^^^


def cyfryKrotne(n):
    T = [0] * 9
    #
    while n > 0:
        T[ n % 10 ] += 1
        n = n // 10
    #end while

    cyfry_jednokrotne = 0
    cyfry_wielokrotne = 0

    for i in range( len(T) ):
        if T[i] > 1: cyfry_wielokrotne += 1
        elif T[i] == 1: cyfry_jednokrotne += 1
    #end for
    return cyfry_jednokrotne, cyfry_wielokrotne
#end def ^^^


def prettySort(T):
    n = len(T)
    #
    for i in range( n ):
        cyfry_jednokrotne, cyfry_wielokrotne = cyfryKrotne( T[i] )
        T[i] = ( T[i], cyfry_jednokrotne, cyfry_wielokrotne )
    #
    T = countingSort(T, 2, 1)
    T = countingSort(T, 1, -1)
    return T
#end def ^^^

T = [ 123, 445, 28, 22, 4456 ]
T = prettySort(T)
print(T)

