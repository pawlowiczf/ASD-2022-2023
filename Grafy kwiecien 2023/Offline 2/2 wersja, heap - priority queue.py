from zad5testy import runtests

def parent(i): return (i-1) // 2
def right(i): return 2 * i + 1
def left(i): return 2 * i + 2


class Vertex:
    def __init__(self, vertex, value = 0):
        self.vertex = vertex
        self.value = value
    #
#end class


def heapify(heap, i, n):
    minInd = i
    l = left(i)
    r = right(i)

    if l < n and heap[l].value < heap[minInd].value : minInd = l 
    if r < n and heap[r].value < heap[minInd].value : minInd = r 

    if minInd != i:
        heap[minInd], heap[i] = heap[i], heap[minInd]
        heapify(heap, minInd, n)
    #
#end def ^^^


def extractMin(heap):
    minValue = heap[0]
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop()
    #
    heapify( heap, 0, len(heap) )

    return minValue
#end def ^^^

def insert(heap, node):
    i = len(heap)
    heap.append( node )

    while i > 0 and heap[ parent(i) ].value > heap[i].value:
        heap[ parent(i) ], heap[i] = heap[i], heap[ parent(i) ]
        i = parent(i)
    #
#end def ^^^


def getVertices(edges):
    maxVertex = 0
    for edge in edges:
        a = edge[0]
        b = edge[1]
        maxVertex = max( maxVertex, a )
        maxVertex = max( maxVertex, b )
    #
    return maxVertex + 1
#end def ^^^


def createG(edges):
    n = getVertices(edges)
    G = [ [] for _ in range(n) ]
    #
    for edge in edges:
        a = (edge[0], edge[2])
        b = (edge[1], edge[2])
        G[ edge[0] ].append(b)
        G[ edge[1] ].append(a)
    #
    return G
#end def ^^^

def checkIfContains(S, vertex):
    for v in range( len(S) ):
        if S[v] == vertex:
            return v 
    #
    return -1
#end def ^^^

def addSingularity(G, S):
    for a in range( len(S) - 1 ):
        for b in range( a + 1, len(S) ):
            G[ S[a] ].append( ( S[b], 0 ) )
            G[ S[b] ].append( ( S[a], 0 ) )
    #
    return G
#end def ^^^

    
def Dijkstra(G, S, n, source):
    visitedSingularity = [ False for _ in range( n ) ]
    isSingularity = [ False for _ in range(n) ]

    distance = [ float('inf') for _ in range(n) ] # distance to each vertex from starting vertex
    done = [ False for _ in range(n) ]
    parent = [ None for _ in range(n) ]

    heap = []
    heap.append( Vertex(source) )
    distance[source] = 0
    done[source] = True 

    while heap:
        node = extractMin(heap)
        vertex = node.vertex

        for (neighbour, weight) in G[vertex]:

            if done[neighbour] == False and ( distance[vertex] + weight ) < distance[neighbour] and isSingularity[neighbour] == False:

                distance[neighbour] = distance[vertex] + weight
                parent[neighbour] = vertex
                insert( heap, Vertex(neighbour, distance[neighbour]) )
            #
        #end for 
        if vertex in S:
            for neighbour in reversed(S):
                if neighbour != vertex and visitedSingularity[neighbour] == False:

                    if distance[vertex]  < distance[neighbour]:
                        distance[neighbour] = distance[vertex]
                        parent[neighbour] = vertex
                        visitedSingularity[neighbour] = True 
                        insert( heap, Vertex(neighbour, distance[neighbour]) )
                        S.pop()
        #end if
        done[vertex] = True
    #end while
    return distance
#end def ^^^


def spacetravel( n, E, S, a, b ):
    n = getVertices( E )
    G = createG( E )
    # G = addSingularity(G, S)

    distance = Dijkstra(G, S, n, a)

    if distance[b] == float('inf'): return None
    return distance[b]

#end def ^^^

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )


# n=7
# E=[(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
# S=[0, 2, 3]
# a=1
# b=5


# print( spacetravel( n, E, S, a, b ) )