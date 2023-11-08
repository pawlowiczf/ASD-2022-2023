from zad1testy import runtests


def Jump(T):
    #
    n = len(T)
    F = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]


    def rek(i, f):
        #
        if i == n - 1: return 0
        f = min( f + T[i], n - 1 )

        if F[i][f] == float('inf'):
            for j in range(1, f + 1):
                if i + j < n:
                    F[i][f] = min( F[i][f], rek(i + j, min( f - j, n - 1 ) ) + 1 )
        #

        return F[i][f]
    #end def rek()

    return rek( 0, 0 )

#end procedure Jump()


def zbigniew( A ):
    #
    return Jump(A)
#

runtests( zbigniew ) 
