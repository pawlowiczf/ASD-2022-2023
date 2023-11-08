"""
po kolei dodajemy wierzcholki w kolejnosci malejacych wag i w ktorym momencie mozemy dojsc do konca, waga ostatniej krawedzi jaka dodalismy
to jest ta minimalna pojemnosc autobusu

Puszczamy grupke ta sama sciezka, ale tak, zeby poscic tych grup jak najmniej 
Posortuj krawedzie malejaco
Rob mst, fragment tego mst wykorzystaj 
maksymalne drzewo rozpinajace 
do kolejki wrzucaj wagi z minusami, wtedy dostaniesz najwieksze drzewo rozpianajace 

bfs, jest tylko jedna sciezka miedzy tymi wierzcholkami start i koniec 
"""
from math import ceil 


class Node:
    def __init__(self, id):
        self.parent = self 
        self.id = id 
        self.rank = 0
#end Class


def Union(X, Y):
    #
    if X.rank > Y.rank:
        Y.parent = X
    elif Y.rank > X.rank:
        X.parent = Y 
    else:
        X.parent = Y 
        X.rank += 1 
#end procedure Union()


def Find(X):
    #
    if X.parent != X:
        X.parent = Find( X.parent )
    
    return X.parent 
#end procedure Find()


def getEdges( A ):
    #
    n = len(A)
    edges = [] 

    for a in range( n - 1 ):
        for b in range( a + 1, n ):
            weight = A[a][b] 
            edges.append( (a, b , weight) )
    #end for loops 

    return edges 
#end procedure getEdges()


def Kruskal( numberOfVertices, ListOfEdges ):
    #
    minSpanningTree = [] 
    Vertices   = [ Node( vertex ) for vertex in range( numberOfVertices ) ]

    ListOfEdges.sort( key = lambda x: x[2], reverse = True ) # posortowanie krawedzi wedlug wag rosnaco 

    for edge in ListOfEdges:
        #
        a, b, weight = edge # wierzcholek 1, wierzcholek 2, waga krawedzi 

        rootX, rootY = Find( Vertices[a] ), Find( Vertices[b] ) # znalezienie korzenia danego wierzcholka w drzewie struktury Find-Union 

        if rootX != rootY:
            minSpanningTree.append( (a, b, weight) )
            Union( rootX, rootY )
        #end 'if' clause

        if len( minSpanningTree ) == numberOfVertices - 1: return minSpanningTree, numberOfVertices 
    #end 'for' loop 

    return minSpanningTree, numberOfVertices 
#end procedure Kruskal()


def getNumberOfVertices( Edges ):
    n = 0 
    for edge in Edges:
        a, b, weight = edge 
        n = max( n, a, b)
    #
    return n + 1 
#end procedure getNumberOfVertices()


def createGraph( numberOfVertices, minSpanningTree ):
    #
    G = [ [] for _ in range( numberOfVertices ) ]

    for edge in minSpanningTree:
        a, b, weight = edge 
        G[a].append( (b, weight) )
        G[b].append( (a, weight) )
    #end 'for' loop 

    return G
#end procedure createGraph()


def DFS( G, visited, parent, vertex ):
    #
    visited[vertex] = True 

    for (neighbour, weight) in G[vertex]:
        if visited[neighbour] == False:
            parent[neighbour] = (vertex, weight)
            DFS(G, visited, parent, neighbour)
    #end 'for' loop 

#end procedure DFS()


def getMinWeight( parent, vertex ): # vertex w domysle to destination
    #
    minWeight = float('inf')
    
    while parent[vertex] != None:
        vertex, weight = parent[vertex]
        minWeight = min( minWeight, weight )
    #end 'while' loop 

    minWeight = min( minWeight, weight )
    return minWeight 
#end procedure getMinWeight()


def guideProblem( Edges, start, destination, numberOfPeople ):
    #
    numberOfVertices = getNumberOfVertices( Edges )
    minSpanningTree, size  = Kruskal( numberOfVertices, Edges )
    G = createGraph( size, minSpanningTree )

    visited = [ False for _ in range( size ) ]
    parent  = [ None  for _ in range( size ) ]
    DFS(G, visited, parent, start)

    return ceil( numberOfPeople / getMinWeight( parent, destination ) )
#end procedure guideProblem()


Edges = [(0, 1, 12), (0, 2, 10), (1, 3, 11), (1, 4, 7), (2, 4, 8), (2, 6, 14), (3, 5, 8), (4, 6, 8), (5, 7, 11), (6, 7, 6)]
print( guideProblem(Edges, 0, 7, 20) )


Eedges = [(0, 1, 50),(0, 3, 25),(1, 2, 75),(2, 3, 20),(3, 5, 50),(5, 6, 2),(4, 6, 10),(6, 7, 20),(7, 8, 70),(1, 5, 75),(2, 5, 30),(3, 4, 50)]
print( guideProblem(Edges, 0, 8, 100) )