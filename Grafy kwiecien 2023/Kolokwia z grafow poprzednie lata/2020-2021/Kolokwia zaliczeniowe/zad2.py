from zad2testy import runtests
from collections import deque 


class Graph:
    def __init__(self, G):
        self.G = G
        self.n = len(G)
        self.visited = [ False for _ in range( self.n ) ]
        self.low     = [ None for _ in range( self.n )  ]
        self.depth   = [ None for _ in range( self.n )  ]
        self.articulationPointVertices = []
        self.time = 0
        self.adjList = G
#end class Graph

def ArticulationPoints(G, root, vertex, parent):
    #
    G.low[vertex]   = G.time 
    G.depth[vertex] = G.time 
    G.time += 1

    children = 0
    G.visited[vertex] = True 

    for neighbour in range( G.n ):
        if G.adjList[vertex][neighbour] == 1:
            if G.visited[neighbour] == False:
                children += 1 
                ArticulationPoints(G, root, neighbour, vertex)
                G.low[vertex] = min( G.low[vertex], G.low[neighbour] )

                if G.low[neighbour] >= G.depth[vertex] and vertex != root:
                    G.articulationPointVertices.append(vertex)
                elif vertex == root and children >= 2:
                    G.articulationPointVertices.append(vertex)

            elif neighbour != parent:
                G.low[vertex] = min( G.low[vertex], G.depth[neighbour] )
        # ----



def BFS(G, vertexRemoved, visited, vertex):
    #
    n = len(G)
    stack = deque()

    visited[vertex] = True 
    stack.append(vertex)

    while stack:
        vertex = stack.popleft()

        for neighbour in range(n):
            
            if G[vertex][neighbour] == 1 and visited[neighbour] == False and neighbour != vertexRemoved:
                visited[neighbour] = True
                stack.append( neighbour )
        #end for
    #end while

#end procedure BFS()


def breaking(G):
    #
    GraphStructure = Graph(G)
    ArticulationPoints( GraphStructure, 0, 0, None)

    numberOfComponents = 0
    whichVertex = None

    for vertexRemoved in GraphStructure.articulationPointVertices:
        visited = [ False for _ in range( GraphStructure.n ) ]
        counter = 0

        for vertex in range( GraphStructure.n ):
            if visited[vertex] == False and vertex != vertexRemoved:
                counter += 1
                BFS(G, vertexRemoved, visited, vertex)
        #end for 

        if counter >= numberOfComponents:
            numberOfComponents = counter
            whichVertex = vertexRemoved
    #end for 

    if numberOfComponents == 1: 
        return None 
    return whichVertex

# end procedure breaking()

runtests( breaking )