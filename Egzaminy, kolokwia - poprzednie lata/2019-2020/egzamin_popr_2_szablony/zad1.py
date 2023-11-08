from zad1testy import runtests

def FloydWarshall(L):
    #
    n = len(L)
    D = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]

    for a in range(n): D[a][a] = 0
    
    for a in range(n):
        for b in L[a]:
            D[a][b] = 1 
            D[b][a] = 1 
    #

    for t in range(n):
        for a in range(n):
            for b in range(n):
                D[a][b] = min( D[a][b], D[a][t] + D[t][b] )
    #

    return D
#end procedure FloydWarshall()


def best_root( L ):
    #
    n = len(L)
    D = FloydWarshall(L)

    bestRoot = -1 
    bestLength = float('inf')

    for vertex in range(n):

        furthestLength = -float('inf')

        for neighbour in range(n):

            if D[vertex][neighbour] > furthestLength and D[vertex][neighbour] != float('inf'):
                furthestLength = D[vertex][neighbour]
        #

        if furthestLength < bestLength:
            bestLength = furthestLength
            bestRoot   = vertex
        #

    #end 'for' loop

    return bestRoot 
#end procedure best_root()


runtests( best_root ) 
