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




def shorthestPath(graph, s, t):
    if s == t:
        return 0
    
    for neighbour, weight in graph.adjList[s]:
        if graph.visited[neighbour] == False:
            graph.visited[neighbour] = True
            dist = shorthestPath(graph, neighbour, t)
            if dist != None:
                result = min( graph.distance[s], shorthestPath(graph, neighbour, t) + weight )
                if result != graph.distance[s]:
                    graph.distance[s] = result 
        #
    #
    return graph.distance[s]
#end def ^^^



class Graph:
    def __init__(self, G):
        self.distance = [ float('inf') for _ in range( len(G) ) ]
        self.visited = [ False for _ in range( len(G) ) ]
        self.adjList = G
    #
#end class

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


G = createG(edges)
graph = Graph(G)
shorthestPath(graph, 0, 8)
print( graph.distance )




