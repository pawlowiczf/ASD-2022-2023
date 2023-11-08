from zad5ktesty import runtests

def Karty( A ):
    n = len(A)
    F = [ [ -1 for _ in range(n) ] for _ in range(n) ]

    def rek(a, b):
        #
        if a == b:
            return A[a] 
        #
        if b - a == 1:
            return max( A[b], A[a] )
        
        if F[a][b] == -1:
            F[a][b] = max( A[a] + min( rek(a + 2, b), rek(a + 1, b - 1) ), A[b] + min( rek(a + 1, b - 1), rek(a, b - 2) ) )
        #end 'if' clause 
        
        return F[a][b]
    #end procedure rek()

    return rek(0, n - 1)
#end procedure Karty()


def garek ( A ):
    #
    return Karty( A )

runtests ( garek )