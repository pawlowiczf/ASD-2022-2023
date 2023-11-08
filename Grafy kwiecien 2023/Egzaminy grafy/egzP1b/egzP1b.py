from egzP1btesty import runtests 
from queue import PriorityQueue


def getVertices( Edges ):
    #
    n = 0 
    for edge in Edges:
        a, b, weight = edge 
        n = max(n, a, b)
    #
    return n + 1
#end def 


def createG( Edges ):
    #
    n = getVertices( Edges )
    G = [ [] for _ in range(n) ]

    for edge in Edges:
        a, b, weight = edge 
        G[a].append( (b, weight) )
        G[b].append( (a, weight) )
    #
    return G
#ned def 


def Dijkstra(G, D, L):
    #
    n = len(G)
    distance = [ [ float('inf') for _ in range(5) ] for _ in range(n) ]

    queue = PriorityQueue()
    queue.put( (0, 0, D) ) # queue.put( ( value, howManyVisitedBefore, vertex ) )
    distance[ D ][ 0 ] = 0

    while not queue.empty():
        #
        value, numberOfVisited, vertex = queue.get()
        if vertex == L: return distance[vertex][4]

        for (neighbour, weight) in G[vertex]:
            #
            if numberOfVisited + 1 <= 3 and distance[vertex][numberOfVisited] + weight < distance[neighbour][ numberOfVisited + 1 ] and neighbour != L:

                distance[neighbour][ numberOfVisited + 1 ] = distance[vertex][numberOfVisited] + weight
                queue.put( ( distance[neighbour][ numberOfVisited + 1], numberOfVisited + 1, neighbour ) )

            elif numberOfVisited + 1 == 4:
                if neighbour == L:
                    distance[neighbour][ numberOfVisited + 1 ] = distance[vertex][numberOfVisited] + weight
                    queue.put( ( distance[neighbour][ numberOfVisited + 1], numberOfVisited + 1, neighbour ) )

        #end 'for' loop
    #end 'while' loop 
    return distance[L][4]
#end procedure Dijkstra()


def turysta( G, D, L ):
    #
    G = createG( G )
    return Dijkstra(G, D, L)
#end def 

runtests ( turysta )