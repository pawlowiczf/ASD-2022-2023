"""
Rekurencyjne schody Amazona
Dana jest tablica A zawierajaca liczby naturalne nie mniejsze od 1. Poczatkowo
stoimy na pozycji 0, wartosc A[i] informuje nas jaka jest maksymalna dlugosc skoku
na nastepna pozycje. 

Przyklad A = [1,3,2,1,0]
Z pozycji 0 moge przejsc na pozycje 1, z pozycji 1 moge przejsc na 2,3,4

Nalezy policzyc na ile sposobow moge przejsc z pozycji 0 na pozycje n-1,
przestrzegajac regul tablicy.
"""


def StairsRek(A):
    #
    n = len(A)
    F = [ 0 for _ in range(n) ]

    def rek(i):
        #
        if i == n - 1: return 1 
        if i >= n: return 0
        
        if F[i] == 0:
            #
            for k in range(1, A[i] + 1):
                F[i] += rek( i + k )
        #
        
        return F[i]
    #end def 

    return rek(0)
#end procedure Stairs()


def Stairs(A):
    #
    n = len(A)
    F = [ 0 for _ in range(n) ]
    F[n-1] = 1

    for a in range(n - 2, -1, -1):
        for b in range(1, A[a] + 1):
            if a + b < n:
                F[a] += F[a + b] 
    #end 'for' loops 
    
    return F[0]
#end def Stairs


def count_jumps_bu(A):
    n = len(A)
    counts = [0] * n
    counts[0] = 1
    
    for i in range(n - 1):
        for j in range(i + 1, min(i + 1 + A[i], n)):
            counts[j] += counts[i]

    return counts[n - 1]
#end def jumps()


A = [10, 6, 4, 4, 9, 10, 2, 3, 3, 6, 7, 0]
print( StairsRek(A) )
print( Stairs(A) )
