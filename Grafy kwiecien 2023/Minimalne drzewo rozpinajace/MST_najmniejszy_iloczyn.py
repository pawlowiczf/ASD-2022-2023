"""
Minimum Product Spanning Tree
"""
import math
from queue import PriorityQueue

def Prims(G):
    #
    n = len(G)
    parent = [ None for _ in range(n) ]
    processed = [ False for _ in range(n) ]
    weights = [ float('inf') for _ in range(n) ]

    queue = PriorityQueue()
    queue.put( (0, 0) )
    weights[0] = 0

    while not queue.empty():
        value, vertex = queue.get()

        if processed[vertex] == False:
            processed[vertex] = True 

            for (neighbour, weight) in G[vertex]:
                if processed[neighbour] == False and weight < weights[neighbour]:

                    parent[neighbour] = vertex
                    weights[neighbour] = weight
                    queue.put( ( math.log(weight), neighbour) )
        #end for

    #end while  
    return parent, weights
#end Prims()


def getMST(G):
    #
    n = len(G)
    G = transformGraph(G)
    parent, weights = Prims(G)
    minProductCost = 1

    for v in range(1, n):
        minProductCost *= weights[v]
    #
    return minProductCost
#end procedure getMST(G)


def transformGraph(G):
    n = len(G)
    newG = [ [] for _ in range(n) ]
    
    for y in range(n):
        for x in range(n):
            if G[y][x] > 0: 
                newG[y].append( ( x, G[y][x] ) )
                newG[x].append( ( y, G[y][x] ) )
                G[x][y] = 0
    #end for's
    return newG
#end procedure transformGraph()


G = [ [ 0, 2, 0, 6, 0 ],
        [ 2, 0, 3, 8, 5 ],
        [ 0, 3, 0, 0, 7 ],
        [ 6, 8, 0, 0, 9 ],
        [ 0, 5, 7, 9, 0 ] ]

print( getMST(G) )
