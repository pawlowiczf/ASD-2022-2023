from zad8testy import runtests
from math import sqrt
from math import ceil 

"""
Minimalne drzewo rozpinające o , ktorego roznica miedzy dlugoscia najkreotszego i najmniejszego jest najmniejsza
Kruskal od najmniejszego wierzcholka 
Wywal z kolejki minimalna krawedz, ktora miales na poczatku (budujesz nowe MST, bez tej krawedzi)


Tworzysz graf pelny, bierzesz od poczatku listy i tworzysz MST ( te o najmniejszej wadze )
zapisujesz dlugosc mst bez tej krawedzi 
Nie tworz MST, jesli nie bedziesz miec odpowiednio duzo krawedzi 
Skoro MST ma n-1 krawedzi, to 


Wzorcowka:
- robimy caly czas MST od nowa
mozna zrobic to drzewo rozpinajace tylko raz, dodac w miejsce starej krawedzi, nowa krawedz, 
second best minimum tree 



"""


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0
    #
#end Class


def Find(x):
    if x.parent != x:
        x.parent = Find( x.parent )
    #
    return x.parent
#end procedure Find()


def Union(X, Y): # X - root, Y - root 
    #
    if X.rank > Y.rank:
        Y.parent = X

    elif X.rank < Y.rank:
        X.parent = Y

    else:
        X.parent = Y 
        Y.rank += 1
#end procedure Union()


def Kruskal( A, Edges, i, minSpanningTree ):
    #
    n = len(A)

    Vertices = [ Node(vertex) for vertex in range(n) ]

    minWeight = Edges[i][2]

    for edge in Edges[ i : len(Edges) ]:
        #
        a, b, weight = edge 
        rootA, rootB = Find( Vertices[a] ), Find( Vertices[b] )

        if rootA != rootB:
            Union( rootA, rootB )
            minSpanningTree.append( (a, b, weight) )
        #

        if len( minSpanningTree ) == n - 1: return minSpanningTree[ n - 2 ][ 2 ] - minWeight, n - 1, minSpanningTree
    #end 'for' loop 

    length = len( minSpanningTree )
    maxWeight = minSpanningTree[ length - 1 ][ 2 ]

    return maxWeight - minWeight, len( minSpanningTree ), minSpanningTree
#end procedure Kruskal()


def calculateLength(A, a, b):
    #
    y1, x1 = A[a]
    y2, x2 = A[b]

    return ceil ( sqrt( ( y2 - y1 ) ** 2 + ( x2 - x1 ) ** 2 ) )
#end procedure calculateLength()


def createEdgesList( A ):
    #
    n = len(A)
    edges = []

    for a in range( n ):
        for b in range( a + 1, n ):
            length = calculateLength(A, a, b)
            edges.append( (a, b, length) )
    #end 'for' loops 

    return edges 
#end procedure createEdgesList()           


def highway( A ):
    #
    n = len(A)

    Edges = createEdgesList( A )
    Edges.sort( key = lambda x: x[2] )

    minDifference = float('inf')
    minSpanningTree = []

    for i in range( len(Edges) ):
        #
        difference, lengthOfTree, minSpanningTree = Kruskal(A, Edges, i, minSpanningTree)

        if lengthOfTree != n - 1: return minDifference 
        if difference < minDifference:
            minDifference = difference
        #
        minSpanningTree.pop(0)
    #end 'for' loop 

    return minDifference
#end procedure highway()

    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )


