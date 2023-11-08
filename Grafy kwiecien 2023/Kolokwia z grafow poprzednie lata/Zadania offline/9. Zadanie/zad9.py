from copy import deepcopy
from queue import PriorityQueue


def relax(distance, vertex, neighbour, weight):
    #

    if distance[vertex] + weight < distance[neighbour]:
        return True 
    return False 

#end procedure relax()


def Dijkstra(G, start, end):
    #
    n = len(G)

    processed = [ False for _ in range(n)        ]
    parent    = [ None for _ in range(n)         ]
    distance  = [ float('inf') for _ in range(n) ]

    queue = PriorityQueue()
    queue.put( (0, start) )
    distance[start] = 0
    processed[start] = True 

    while not queue.empty():
        #
        value, vertex = queue.get()

        if vertex == end: return distance, parent

        if value == distance[vertex]:
            for neighbour in range(n):

                weight = G[vertex][neighbour]

                if weight != -1 and not processed[neighbour]:
                    if relax( distance, vertex, neighbour, weight ):

                        distance[neighbour] = distance[vertex] + weight
                        queue.put( ( distance[neighbour], neighbour ) )
                        parent[neighbour] = vertex

                #end 'if' clauses

            #end 'for' loop 
        #end 'if' clause 
        processed[vertex] = True 

    #end 'while' loop
    return False, False
#end procedure Dijkstra()


def restoreCycle(G, parent, a, b):
    #
    cycle = []

    while b != None:
        cycle.append(b)
        b = parent[b] 
    #end while 

    return cycle 
#end procedure restoreCycle()


def min_cycle(G):
    #
    n = len(G)

    vertices = None 
    minLength = float('inf')

    for a in range( n ):
        for b in range( n ):
            if a != b and G[a][b] > -1:

                weight = G[a][b]
                G[a][b] = -1
                G[b][a] = -1

                distance, parent = Dijkstra(G, a, b)

                G[a][b] = weight 
                G[b][a] = weight 

                if distance:
                    length = distance[b] + weight
                    if length < minLength:

                        minLength = length 
                        vertices = (a, b) 
                        parentList = parent 
                #end if 
            #end if 
    #end 'for's loop
    if vertices:
        a, b = vertices
        print( minLength )
        return restoreCycle(G, parentList, a, b)
    else:
        return -1
#end procedure min_cycle()


G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]
LEN = 7


GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)


if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")


G = [[-1, 1,-1, 4, 1],
     [ 1,-1, 1,-1, 4],
     [-1, 1,-1, 1, 4],
     [ 4,-1, 1,-1, 1],
     [ 1, 4, 4, 1,-1]]

LEN = 5
print( min_cycle(G) )

G = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
     [4, -1, 8, -1, -1, -1, -1, 11, -1],
     [-1, 8, -1, 7, -1, 4, -1, -1, 2],
     [-1, -1, 7, -1, 9, 14, -1, -1, -1],
     [-1, -1, -1, 9, -1, 10, -1, -1, -1],
     [-1, -1, 4, 14, 10, -1, 2, -1, -1],
     [-1, -1, -1, -1, -1, 2, -1, 1, 6],
     [8, 11, -1, -1, -1, -1, 1, -1, 7],
     [-1, -1, 2, -1, -1, -1, 6, 7, -1]]
LEN = 14

print( min_cycle(G) )


def undirected_weighted_graph_matrix(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[-1] * n for _ in range(n)]  # -1 means no edge
    for e in E:
        G[e[0]][e[1]] = e[2]
        G[e[1]][e[0]] = e[2]
    return G
	
	
E = [(0, 1, 3), (1, 2, 2), (0, 6, 2), (6, 7, 1), (6, 5, 3), (5, 7, 1),
    (5, 4, 8), (3, 4, 20), (8, 7, 7), (8, 1, 1), (2, 3, 5), (3, 8, 1),
    (7, 4, 2)]
LEN = 5
G =  undirected_weighted_graph_matrix(E)
print( min_cycle(G) )

E = [(0, 1, 9), (1, 2, 18), (2, 3, 15), (3, 4, 20), (4, 5, 5), (5, 6, 5), (6, 7, 7), (7, 8, 10), (8, 9, 8),
     (0, 15, 10), (1, 15, 4), (1, 14, 5), (15, 14, 4), (14, 3, 10), (15, 13, 6), (13, 14, 5), (16, 15, 6),
     (16, 13, 2), (18, 17, 2), (17, 16, 3), (16, 12, 5), (12, 13, 4), (13, 11, 10), (11, 10, 4),
     (12, 10, 12), (10, 5, 10), (11, 4, 6)]
LEN = 11
G =  undirected_weighted_graph_matrix(E)
print( min_cycle(G) )

E = [(0, 1, 17), (1, 2, 30), (2, 3, 2), (3, 4, 47), (4, 5, 88), (5, 6, 0), (7, 6, 3), (7, 8, 7), (8, 9, 0), (9, 10, 12),
     (10, 11, 40), (11, 0, 13), (11, 14, 1), (14, 12, 7), (12, 13, 18), (13, 1, 120), (3, 16, 81), (16, 15, 63),
     (15, 17, 90), (17, 5, 37), (11, 23, 0), (23, 22, 67), (22, 21, 73), (21, 24, 11), (24, 23, 2), (21, 20, 18),
     (20, 19, 96), (19, 18, 50), (18, 29, 4), (29, 20, 22), (18, 5, 1), (21, 25, 97), (25, 26, 26), (26, 27, 30),
     (27, 28, 8), (28, 20, 11), (26, 30, 100), (30, 27, 52), (30, 31, 1), (31, 32, 20), (31, 33, 0), (34, 26, 4),
     (35, 26, 3), (36, 26, 2), (27, 37, 10), (27, 38, 8), (27, 39, 1)]
LEN = 120
G =  undirected_weighted_graph_matrix(E)
print( min_cycle(G) )