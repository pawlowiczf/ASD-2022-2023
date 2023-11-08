from zad1ktesty import runtests


def BinarySubstring( S ):
    #
    n = len(S)
    F = [ [ 0 for _ in range(n) ] for _ in range(n) ]

    for k in range(n):
        if S[k] == "1":
            F[k][k] = -1 
        else:
            F[k][k] = 1
    #

    best = -1 
    for a in range(1, n - 1):
        for b in range(a + 1, n):

            if S[b] == "1":
                F[a][b] = F[a][b - 1] - 1
            elif S[b] == "0":
                F[a][b] = F[a][b - 1] + 1  

            best = max( best, F[a][b] )

    #end 'for' loops 

    return best 
#end procedure BinarySubstring()


def roznica( S ):
    #
    return BinarySubstring( S )
#end procedure roznica()

runtests ( roznica )