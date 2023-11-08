from egzP5btesty import runtests 


class Graph:
    def __init__(self, adjList):
        self.n = len( adjList )
        self.adjList = adjList

        self.low   = [ None for _ in range( self.n ) ]
        self.depth = [ None for _ in range( self.n ) ]
        self.visited = [ False for _ in range( self.n ) ]

        self.articulationPoint = [ False for _ in range( self.n ) ]
        self.counter = 0
    #
#end Class 


def ArticulationPoint(G, root, vertex, parent):
    #
    G.visited[vertex] = True
    G.depth[vertex] = G.counter
    G.low[vertex] = G.counter 
    G.counter += 1 

    children = 0
    for neighbour in G.adjList[vertex]:

        if G.visited[neighbour] == False:

            children += 1
            ArticulationPoint(G, root, neighbour, vertex)
            G.low[vertex] = min( G.low[vertex], G.low[neighbour] )

            if G.low[neighbour] >= G.depth[vertex]:
                if vertex != root or children >= 2:
                    G.articulationPoint[vertex] = True 
        
        elif parent != neighbour:
            G.low[vertex] = min( G.low[vertex], G.depth[neighbour] )

        #end 'if' clauses

    #end 'for' loop 
#end procedure ArticulationPoint()


def getVertices( B ):
    #
    n = 0 
    
    for (start, end) in B:
        n = max(n, start, end)
    #
    return n + 1
#end procedure getVertices()


def createG( B ):
    #
    n = getVertices( B )
    G = [ [] for _ in range(n) ]

    for (start, end) in B:
        G[start].append(end)
        G[end].append(start)
    #end 'for' loop 

    return G
#end procedure createG()


def koleje ( B ):
    #
    G = createG( B )
    G = Graph(G)

    ArticulationPoint(G, 0, 0, None)
    number = 0

    for vertex in range( G.n ):
        if G.articulationPoint[vertex] == True:
            number += 1
    #
    return number
#end procedure koleje()

runtests ( koleje, all_tests=True )