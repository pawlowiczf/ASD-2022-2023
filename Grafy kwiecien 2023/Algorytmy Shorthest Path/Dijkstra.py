

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


from queue import PriorityQueue

def Dijkstra(edges, source):
    n = getVertices(edges)
    G = createG(edges)

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
        value = node.value

        for (neighbour, weight) in G[vertex]:
            if distance[vertex] == value: # optymalizacja 
                if done[neighbour] == False and ( distance[vertex] + weight ) < distance[neighbour]:

                    distance[neighbour] = distance[vertex] + weight
                    parent[neighbour] = vertex
                    insert( heap, Vertex(neighbour, distance[neighbour]) )
            #
        #end for 
        done[vertex] = True
    #end while
    return distance
#end def ^^^


edges = [
    (0,1,4),
    (1,7,11),
    (0,7,8),
    (1,2,8),
    (7,8,7),
    (7,6,1),
    (6,8,6),
    (8,2,2),
    (2,3,7),
    (2,5,4),
    (6,5,2),
    (3,5,14),
    (3,4,9),
    (5,4,10)
]

distance = Dijkstra(edges, 0)

for i in range( getVertices(edges) ):
    print(f"Z wierzcholka 0 do wierzcholka {i}: {distance[i]}")




   
