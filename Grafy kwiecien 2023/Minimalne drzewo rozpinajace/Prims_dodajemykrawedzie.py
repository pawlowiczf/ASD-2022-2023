from queue import PriorityQueue 

def createG(edges):
    n = 0 
    for edge in edges:
        n = max( n, edge[0], edge[1] )
    #
    n += 1 
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a, b, weight = edge[0], edge[1], edge[2]
        G[a].append( (b, weight) )
        G[b].append( (a, weight) )
    #
    return G
#end procedure createG()


def vertex(edges):
    n = 0 
    for edge in edges:
        n = max( n, edge[0], edge[1] )
    #
    return n + 1
#end procedure vertex()


def Prims(G):
    #
    n = len(G)
    processed = [ False for _ in range(n) ]

    minSpanningTree = []
    costTree = 0
    lenTree = 0 
    queue = PriorityQueue()


    processed[0] = True 
    for vertex, weight in G[0]:
        queue.put( (weight, 0, vertex) )

    while not queue.empty():
        #
        value, firstVertex, secondVertex = queue.get()
        if processed[secondVertex] == False:
            minSpanningTree.append( (firstVertex, secondVertex, value) )
            costTree += value
            
            lenTree += 1
            if lenTree == n - 1: return costTree

            for (neighbour, weight) in G[ secondVertex ]:
                if processed[neighbour] == False:
                    queue.put( (weight, secondVertex, neighbour) )
            #
        processed[secondVertex] = True 

    #end while 
    return costTree
#end procedure Prims()


E = [(0, 1, 9), (1, 4, 3), (4, 6, 6), (6, 5, 1), (5, 2, 6), (2, 0, 0), (0, 5, 7), (0, 3, 5), (3, 5, 2), (3, 1, -2), (3, 6, 3)]
G = createG(E)
print( Prims(G) ) # 9


E = [(0, 1, 2), (1, 3, 0), (0, 3, 2), (0, 4, 3), (0, 2, 5), (2, 3, 1), (2, 4, 6), (4, 3, 4), (3, 5, 8)]
G = createG(E)
print( Prims(G) ) # 14 

E = [(0, 1, 6), (1, 2, 4), (3, 4, 1), (4, 5, 7), (6, 7, 11), (7, 8, 5), (0, 3, 3), (3, 6, 8), (1, 4, 2), (4, 7, 9), (2, 5, 12), (5, 8, 10)]
G = createG(E)
print( Prims(G) ) # 39

E = [(0, 1, 1), (1, 2, 5), (2, 3, 3000), (0, 5, 12), (1, 5, 7), (5, 2, 6), (5, 4, 8), (4, 2, 4), (4, 3, 9)]
G = createG(E)
print( Prims(G) ) # 25
