"""
Algorytm, na szukanie mostow 
Given an undirected connected graph, check if the graph is 2-edge connected and return the bridges (if any).

A connected graph is 2-edge connected if it remains connected whenever any edges are removed. A bridge (or cut arc) is an edge of a graph 
whose deletion increases its number of connected components, 
i.e., an edge whose removal disconnects the graph. 
So if any such bridge exists, the graph is not 2-edge connected.
"""


# DFS

def SearchBridges(G, v, visited, arrival, bridges, parent, time ):
    time += 1
    visited[v] = True 
    arrival[v] = time 
    ArrivalTime = time # = arrival[v]

    for vertex in G[v]:

        if visited[vertex] == False:
            ArrivalTime = min( ArrivalTime, SearchBridges(G, vertex, visited, arrival, bridges, v, time) )
        
        elif vertex != parent:
            ArrivalTime = min( arrival[vertex], arrival[v] )
    #

    if ArrivalTime == arrival[v] and parent != -1: # musimy dodac warunek parent != -1, bo w przeciwnym razie traktowalibysmy krawedz (-1, 0) jako most, ale takiej nie ma
        bridges.append( (parent, v) )


    return ArrivalTime 
#end def ^^^


def Bridges(G):
    n = len(G)
    
    visited = [ False for _ in range(n) ]
    arrival = [ None for _ in range(n)  ]
    bridges = []

    SearchBridges(G, 0, visited, arrival, bridges, -1, 0)
    return bridges
#end def ^^^


def Edge(G, u, v):
    G[u].append(v)
    G[v].append(u)
#

V = 6
G = [ [] for _ in range(V) ]
Edge(G, 0, 2)
Edge(G, 1, 2)
Edge(G, 2, 3)
Edge(G, 2, 4)
Edge(G, 3, 4)
Edge(G, 3, 5)

bridges = Bridges(G)
print(bridges)




def createG(edges, n):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a, b = edge[0], edge[1]
        G[a].append(b)
        G[b].append(a)
    #end for 
    return G
#end procedure createG

E = [(0, 1), (1, 2), (2, 0), (3, 1), (3, 0), (4, 3), (5, 3), (5, 7), (5, 6), (6, 7), (0, 8), (8, 9),
     (9, 10), (8, 10), (10, 11), (11, 12), (12, 13), (11, 13)]

G = createG(E, 14)
bridges = Bridges(G)
print(bridges)