from zad9testy import runtests
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


def FordFulkerson(Graph, s, t): # M - graf reprezentowany w postaci macierzowej, s - zrodlo, t - ujscie
    #
    n = len(Graph)
    G = [ [ Graph[a][b] for b in range(n) ] for a in range(n) ]

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

def createMatrix(G):
    #
    n = 0
    for (a, b, value) in G:
        n = max(n, a, b)
    #
    n += 1

    M = [ [ 0 for _ in range(n + 1) ] for _ in range(n + 1) ]

    for (a, b, value) in G:
        M[a][b] = value 
    #
    return M
#end procedure createMatrix()

def maxflow( M, s ):
    #
    G = createMatrix(M)
    
    n = len(G)
    bestFlow = 0 

    for a in range(n - 1):
        for b in range(a + 1, n - 1):

            if a != s and b != s:

                G[a][n - 1] = float('inf')
                G[b][n - 1] = float('inf')

                flow = FordFulkerson(G, s, n - 1)
                bestFlow = max( bestFlow, flow )

                G[a][n - 1] = 0
                G[b][n - 1] = 0

            #
        #
    #end 'for' loops 
    
    return bestFlow 
#end procedure maxflow()

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )