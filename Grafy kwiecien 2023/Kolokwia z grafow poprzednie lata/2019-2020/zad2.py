from zad2testy import runtests
from queue import PriorityQueue

class Graph:
    def __init__(self, G, L, W):
        distance = [ [ float('inf') for _ in range( len(W) ) ] for _ in range( len(L) ) ] 
        self.adjList = G
        self.L = L
        self.W = W
        self.distance = distance
#end class 


def Dijkstra(G, vertex):
    #
    queue = PriorityQueue()
    
    n = len( G.L )
    sizeWord = len( G.W )

    for vertex in range(n):
        if G.L[vertex] == G.W[0]:
            queue.put( ( 0, vertex, 0 ) )
            G.distance[vertex][0] = 0
    #end 'for' loop

    while not queue.empty():
        #
        value, vertex, index = queue.get()
        if index == sizeWord - 1: return G.distance[vertex][index]

        for (neighbour, weight) in G.adjList[vertex]:
            if G.L[neighbour] == G.W[index + 1] and G.distance[vertex][index] + weight < G.distance[neighbour][index + 1]:

                G.distance[neighbour][index + 1] = G.distance[vertex][index] + weight 
                queue.put( (G.distance[neighbour][index + 1], neighbour, index + 1 ) )     

        #end 'for' loop 
    #end 'while' loop 
    return None
#end procedure Dijkstra()


def createG(E, L):
    #
    n = len(L)
    G = [ [] for _ in range(n) ]

    for edge in E:
        a, b, weight = edge
        G[a].append( (b, weight) )
        G[b].append( (a, weight) )
    #end for 
    return G

#end procedure createG()


def letters( G, W ):
    #   
    L, E = G # L - litera w danym wierzcholku, E - lista krawedzi z waga
    n = len(L)

    adjList = createG(E, L)
    G = Graph(adjList, L, W)

    return Dijkstra(G, n)
#end procedure Dijkstra()

runtests( letters )
    
    
# L = ["k", "k", "o", "o", "t", "t"]
# E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
# G = (L, E)
# W = "kto"

# print( letters( (L, E), W) )