# Algorytm Prim'a, dla grafu w postaci listowej

from queue import PriorityQueue


def Prims(G):
    #
    n = len(G)
    processed = [ False for _ in range(n)        ]
    parents   = [ -1  for _ in range(n)          ]
    weights   = [ float('inf') for _ in range(n) ]

    queue = PriorityQueue()
    queue.put( (0, 0) ) # queue.put( value, vertex )
    weights[0] = 0

    while not queue.empty():
        value, vertex = queue.get()

        if not processed[vertex]:
            processed[vertex] = True 
            
            for ( neighbour, weight ) in G[vertex]:

                if not processed[neighbour] and weight < weights[neighbour]:
                    weights[neighbour] = weight
                    parents[neighbour] = vertex 
                    queue.put( (weight, neighbour) )
            #end for 
        #end if 
    #end while 

    return parents, weights
#end procedure Prims()

def createMST(G):
    #
    n = len(G)
    parents, weights = Prims(G)
    newG = [ [] for _ in range(n) ]

    for v in range(n):
        if parents[v] != -1:
            newG[ parents[v] ].append( (v, weights[v] ) )
            newG[ v ].append( (parents[v], weights[v] ) )
    #end for 

    return newG
#end procedure createMST()


# ---------------------------
# Driver's code:

def undirected_weighted_graph_list(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    return G


G = undirected_weighted_graph_list([(0, 1, 1), (1, 2, 5), (2, 3, 3000), (0, 5, 12), (1, 5, 7),
                                    (5, 2, 6), (5, 4, 8), (4, 2, 4), (4, 3, 9)])

print( Prims(G) )
print( createMST(G) )

print(" ----------------- " )

G = undirected_weighted_graph_list([(0, 1, 9), (1, 4, 3), (4, 6, 6), (6, 5, 1), (5, 2, 6), (2, 0, 0),
                                    (0, 5, 7), (0, 3, 5), (3, 5, 2), (3, 1, -2), (3, 6, 3)])

print( Prims(G))
print( createMST(G) )

print(" ----------------- " )

G = undirected_weighted_graph_list([(0, 1, 2), (1, 3, 0), (0, 3, 2), (0, 4, 3), (0, 2, 5), (2, 3, 1),
                                    (2, 4, 6), (4, 3, 4), (3, 5, 8)])

print( Prims(G))
print( createMST(G) )

print(" ----------------- " )

G = undirected_weighted_graph_list([(0, 1, 6), (1, 2, 4), (3, 4, 1), (4, 5, 7), (6, 7, 11), (7, 8, 5),
                                    (0, 3, 3), (3, 6, 8), (1, 4, 2), (4, 7, 9), (2, 5, 12), (5, 8, 10)])

print( Prims(G))
print( createMST(G) )

