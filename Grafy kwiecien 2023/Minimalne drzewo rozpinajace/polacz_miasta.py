"""
There are n cities and there are roads in between some of the cities. 
Somehow all the roads are damaged simultaneously. 
We have to repair the roads to connect the cities again. 
There is a fixed cost to repair a particular road. 
Find out the minimum cost to connect all the cities by repairing roads. 
Input is in matrix(city) form, if city[i][j] = 0 then there is not any road between city i and city j, if city[i][j] = a > 0 
then the cost to rebuild the path between city i and city j is a. 
Print out the minimum cost to connect all the cities. 
It is sure that all the cities were connected before the roads were damaged.

"""


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self 
        self.rank = 0
#end class

def Find(x):
    if x.parent != x:
        x.parent = Find( x.parent )
    #
    return x.parent 

#end procedure Find()

def Union(x, y):
    #
    if x.rank > y.rank:
        y.parent = x
    elif y.rank > x.rank:
        x.parent = y 
    else:
        x.parent = y 
        y.rank += 1

#end procedure Union()

def transformToEdges(G):
    n = len(G)
    edges = []
    
    for y in range(n):
        for x in range(n):
            if G[y][x] > 0: 
                edges.append( (y, x, G[y][x]) )
                G[x][y] = 0
    #end for's
    return edges
#end procedure transformToEdges()

def Kruskal(G):
    #
    n = len(G)

    edges = transformToEdges(G)
    edges.sort( key = lambda x: x[2] )
    Vertices = [ Node(v) for v in range(n) ]

    costToConnect = 0

    for edge in edges:
        a, b, weight = edge 
        rootA, rootB = Find( Vertices[a] ), Find( Vertices[b] )

        if rootA != rootB:
            Union( rootA, rootB )
            costToConnect += weight
        #
    #end for 

    return costToConnect
#end procedure Kruskal()


G =    [ [0, 1, 2, 3, 4],
         [1, 0, 5, 0, 7],
         [2, 5, 0, 6, 0],
         [3, 0, 6, 0, 0],
         [4, 7, 0, 0, 0] ]

print( Kruskal(G) )


G =    [ [0, 1, 1, 100, 0, 0],
         [1, 0, 1, 0, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [100, 0, 0, 0, 2, 2],
         [0, 0, 0, 2, 0, 2],
         [0, 0, 0, 2, 2, 0] ]

print( Kruskal(G) )

    
