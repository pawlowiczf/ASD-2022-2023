from copy import deepcopy
from collections import deque 


def BFS(G, parent, vertex, t): # t - ujscie
    #
    n = len(G)

    visited = [ False for _ in range(n) ] 

    queue = deque()
    queue.append( vertex )
    visited[vertex] = True 

    while queue:
        #
        vertex = queue.popleft()
        
        for neighbour in range(n):
            if visited[neighbour] == False and G[vertex][neighbour] > 0:

                queue.append( neighbour )
                visited[neighbour] = True 
                parent[neighbour]  = vertex
                
                if neighbour == t: return True
        #end for 
    #end while 

    return False # - nie dotarlismy do ujscia, wiec nie ma sciezki powiekszajacej

#end procedure BFS(G, vertex)


def augmentThePath(G, parent, vertex):
    #
    bottleNeck = float('inf') 
    helpVariable = vertex 

    while parent[vertex] != None:

        bottleNeck = min( bottleNeck, G[ parent[vertex] ][ vertex ] )
        vertex = parent[vertex]
    
    #end while 
    
    vertex = helpVariable

    while parent[vertex] != None:

        G[ parent[vertex ] ][ vertex ] -= bottleNeck 
        G[ vertex ][ parent[vertex ] ] += bottleNeck 
        vertex = parent[vertex]

    #end while 
    
    return bottleNeck 
#end procedure augmentThePath


def FordFulkerson(M, s, t): # M - graf reprezentowany w postaci macierzowej, s - zrodlo, t - ujscie
    #
    n = len(M)
    G = deepcopy(M)

    parent  = [ None for _ in range(n) ]
    maxFlow = 0
    #

    while BFS(G, parent, s, t):
        #
        bottleNeck = augmentThePath(G, parent, t)
        maxFlow += bottleNeck 
    #end while 

    return maxFlow 
#end procedure FordFulkerson()


G = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0] ]

print( FordFulkerson(G, 0, 5) ) # 23

G = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]

print( FordFulkerson(G, 0, 5) ) # 6



















