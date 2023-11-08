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


    
def sortEdges(E):
    #
    E.sort( key = lambda x: x[2] )
    return E
#end procedure sortEdges()


def Kruskal(G):
    #
    V, E = G
    minSpanningTree = []
    print(V)
    #
    E = sortEdges(E)
    Vertices = [ Node(v) for v in V ]

    for edge in E:
        #
        a, b, weight = edge
        rootA, rootB = Find( Vertices[a] ), Find( Vertices[b] )

        if rootA != rootB:
            Union( rootA, rootB )
            minSpanningTree.append( edge )
        #end if 
    #end for

    return minSpanningTree
#end procedure Kruskal()


def createG(E):
    """
    This function creates an array of vertices based on the array of edges
    and returns both, array of vertices and array of edges
    """
    return list(set(map(lambda e: e[0], E)) | set(map(lambda e: e[1], E))), E
#end procedure createG()


# Testy:

G = createG([(5, 0, 2), (0, 1, 3), (1, 2, 1), (5, 6, 1), (1, 6, 2), (5, 4, 6),
                  (4, 3, 8), (3, 6, 5), (2, 3, 7)])
print( Kruskal(G) )
# [(1, 2, 1), (5, 6, 1), (5, 0, 2), (1, 6, 2), (3, 6, 5), (5, 4, 6)]
print( " -------" )


G = createG([(0, 5, 1), (0, 1, 2), (1, 2, 7), (5, 6, 3), (6, 1, 8), (5, 4, 2), (4, 6, 5),
                  (4, 3, 6), (3, 2, 4)])
print( Kruskal(G) )
# [(0, 5, 1), (0, 1, 2), (5, 4, 2), (5, 6, 3), (3, 2, 4), (4, 3, 6)]
print( " -------")


G = createG([(0, 1, 7), (1, 2, 1), (2, 3, 12), (3, 4, 6), (4, 5, 5), (0, 5, 2), (0, 3, 3),
                  (0, 2, 8), (2, 4, 4)])
print( Kruskal(G) )
# [(1, 2, 1), (0, 5, 2), (0, 3, 3), (2, 4, 4), (4, 5, 5)]
print( " -------")