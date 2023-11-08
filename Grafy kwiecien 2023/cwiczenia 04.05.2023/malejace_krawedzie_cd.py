"""
Dany jest graf G = (V,E), gdzie kazda krawedz ma wage
ze zbioru {1, . . . , SES} (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, który dla danych
wierzchołków x i y oblicza sciezke o najmniejszej sumie wag, która prowadzi z x do y po krawedziach o
malejacych wagach (jesli sciezki nie ma to zwracamy ª).
"""

# Odpowiednio posortowac krawedzie, wedlug kosztu malejaco 
# Mamy nieskonoczonosci w wierzcohlkach
# DOdajemy do drogi lub nie krawedzie, jesli bylibysmy w stanie polepszyc te nasza odleglosc 

# Bierzemy 
# Jedna iteracja Bellmana-Forda

from queue import PriorityQueue

# def Dijkstra(G, s, t):
#     #
#     n = len(G)

#     distance = [ float('inf') for _ in range(n) ] 
#     distance[s] = 0

#     queue = PriorityQueue()
#     queue.put( (0, s) )

#     # queue.put( value, (state, vertex) ), gdzie state: 0 - doszedlem do wierzcholka nie wykorzystujac butow, 1 - doszedlem wykorzystujac buty 

#     while not queue.empty():
#         value, vertex = queue.get()
#         if vertex == t: return distance[t]

#         for neighbour, weight in G[vertex]:
#             if distance[vertex] + weight < distance[neighbour]:
#                 distance[neighbour] = distance[vertex] + weight
#                 queue.put( (distance[neighbour], neighbour) )
#     #end while 

#     return distance[t] 
# #end procedure Dijkstra()

def descendingEdges(n, edges, x, y):
    #
    G = [ [] for _ in range(n) ]

    edges.sort( key = lambda x: x[2], reverse = True )
    visited = [ False for _ in range(n) ]
    distance = [ float('inf') for _ in range(n) ]

    visited[x] = True 
    distance[x] = 0

    for edge in edges:
        a, b, weight = edge

        if visited[a] == True:
            G[a].append( (b, weight) )
            G[b].append( (a, weight) )
            distance[b] = min( distance[a] + weight, distance[b] )
            visited[b] = True
    #end for 

    # return Dijkstra(G, x, y)
    return distance[y]

#end procedure descendingEdges()


E = [(0, 1, 15), (0, 2, 2), (0, 3, 6), (1, 2, 14), (1, 4, 7), (2, 5, 3), (2, 6, 4), (3, 7, 2),
         (4, 8, 6), (5, 9, 2), (6, 8, 5), (7, 9, 8), (8, 10, 5), (9, 10, 1)]

s = 0
t = 10

print( descendingEdges(11, E, s, t) )

E = [(0, 1, 1), (1, 2, 4), (2, 3, 3), (0, 5, 40), (5, 6, 38), (0, 7, 5), (6, 7, 8), (7, 1, 6),
     (7, 2, 16), (6, 2, 23), (6, 8, 35), (5, 4, 30), (8, 4, 20), (8, 3, 15), (4, 3, 80)]

s, t = 0, 3
print(descendingEdges(9, E, s, t)) # 99 
s, t = 1, 3
print(descendingEdges(9, E, s, t)) # 7
s, t = 3, 1
print(descendingEdges(9, E, s, t)) # inf 
s, t = 2, 0
print(descendingEdges(9, E, s, t)) # 5