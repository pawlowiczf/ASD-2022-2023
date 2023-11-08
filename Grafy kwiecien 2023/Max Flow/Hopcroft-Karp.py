from collections import deque 


class Graph:

    def __init__(self, adjList, n):

        self.n = n
        self.pairU = [ n for _ in range( n ) ] # dopasowania pracownikow do maszyn 
        self.pairV = [ n for _ in range( n ) ] # dopasowania maszyn do pracownikow 
        self.adjList = adjList 

    #end def 
#end class 


def BFS(G, distance):
    #
    queue = deque ()
    n = G.n

    for vertex in range(n):
        if G.pairU[ vertex ] == n:
            
            distance[ vertex ] = 0 
            queue.append( vertex )
    #end for 
    distance[n] = float('inf')

    while queue:
        #
        vertex = queue.popleft()

        if vertex != n:
            for neighbour in G.adjList[ vertex ]:
                if distance[ G.pairV[ neighbour ] ] == float('inf'):

                    queue.append( G.pairV[ neighbour ] )
                    distance[ G.pairV[ neighbour ] ] = distance[ vertex ] + 1 

                #end 'if' clause     
            #end 'for' loop 
        #end 'if' clause 

    #end 'while' loop 

    return distance[n] != float('inf')
#end procedure BFS()


def DFS(G, distance, vertex): # NIL - wierzcholek o indeksie n
    #
    if vertex != G.n:
        
        for neighbour in G.adjList[vertex]: # na pewno sie nie zapetlimy, bo ponizszy if zwroci False dla parent'a
            if distance[ G.pairV[neighbour] ] == distance[ vertex ] + 1:

                if DFS( G, distance, G.pairV[ neighbour ] ):
                    G.pairU[ vertex ]    = neighbour 
                    G.pairV[ neighbour ] = vertex 
                    return True 
                #end 'if' clause 
        #end 'for' loop 

        distance[vertex] = float('inf')
        return False 
    
    #end 'if' clause 
    return True 
#end procedure DFS()


def HopcroftKarp( adjList ):
    #
    G = Graph( adjList, len(adjList) )
    matching = 0

    distance = [ float('inf') for _ in range( G.n + 1 ) ]

    while BFS(G, distance):

        for vertex in range( G.n ):
            if G.pairU[ vertex ] == G.n and DFS(G, distance, vertex):
                matching += 1 
        #end 'for' loop 

        distance = [ float('inf') for _ in range( G.n + 1 ) ]
    #end 'while' loop 
    
    return matching 

#end procedure HopcroftKarp()




adjList = [ [ 0, 1, 3], [ 2, 4],[ 0, 2],[ 3 ], [ 3, 2] ]
print( HopcroftKarp( adjList ) ) # 5
