from egzP3btesty import runtests 
from queue import PriorityQueue

class Node:
    def __init__(self, id):
        self.rank = 0
        self.id = id 
        self.parent = self 
#end Class


def Union(X, Y):
    #
    if X.rank > Y.rank:
        Y.parent = X
    elif Y.rank > X.rank:
        X.parent = Y
    else:
        Y.parent = X
        Y.rank += 1

#end procedure Union()


def Find(X):
    #
    if X.parent != X:
        X.parent = Find( X.parent )
    #
    return X.parent 

#end procedure Find()

    
def createEdgesList(G):
    #
    n = len(G)
    ListOfEdges = []
    totalSumWeight = 0

    for vertex in range(n):
        for (neighbour, weight) in G[vertex]:
            if vertex < neighbour:
                ListOfEdges.append( (vertex, neighbour, weight) )
                totalSumWeight += weight
    #end 'for' loops 

    return ListOfEdges, totalSumWeight
#end procedure createEdgesList()


def Kruskal( G, Edges ):
    #
    n = len(G)

    MaximumSpanningTree = []

    maxWeightEdge = -float('inf')
    sumOfMSTWeight = 0

    Vertices = [ Node(vertex) for vertex in range(n) ]

    for edge in Edges:
        a, b, weight = edge 
        rootA, rootB = Find( Vertices[a] ), Find( Vertices[b] )

        if rootA != rootB:
            Union(rootA, rootB)
            MaximumSpanningTree.append( edge )
            sumOfMSTWeight += weight
        else:
            maxWeightEdge = max( maxWeightEdge, weight )

        if len( MaximumSpanningTree ) == n - 1: return sumOfMSTWeight, maxWeightEdge

    #end 'for' loop
#end procedure Kruskal()



def lufthansa ( G ):
    #
    n = len(G)
    Edges, totalSumWeight = createEdgesList(G)
    Edges.sort( key = lambda x: x[2], reverse = True )
    
    sumOfMSTWeight, maxWeightEdge = Kruskal(G, Edges)
    if maxWeightEdge == -float('inf'): maxWeightEdge = Edges[ n - 1 ][2]

    return totalSumWeight - ( sumOfMSTWeight + maxWeightEdge )
#end procedure lusthansa()

runtests ( lufthansa, all_tests=True )