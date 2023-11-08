"""
Mamy dany graf G = (V,E) z wagami (dodatnie liczby naturalne).
Chcemy znalezc sciezke z wierzchołka u do v tak, by iloczyn wag był minimalny. 
"""

# Wagi dodatnie liczby naturalne
# Sciezka o iloczynie wag najmniejszy
# log(a*b*c) = log(a) + log(b) + log(c) 
# Jak wyciagamy jakis wierzcholek i wage, to odwolujemy sie do jego logarytmu. 

from queue import PriorityQueue
from math import inf, log10

def relax(distance, vertex, neighbour, weight):

    if distance[neighbour] > distance[vertex] + log10(weight):
        distance[neighbour] = distance[vertex] + log10(weight) 
        return True 
    #
    return False 
#end def ^^^


def Dijkstra(G, source):
    n = len(G)
    done     = [ False for _ in range(n) ]
    distance = [ float('inf') for _ in range(n) ]
    parent = [ None for _ in range(n) ]

    queue = PriorityQueue()
    queue.put( (0, source) )
    distance[source] = 0

    while not queue.empty():
        value, vertex = queue.get()

        if distance[vertex] == value:
            for (neighbour, weight) in G[vertex]:
                if done[neighbour] == False and relax(distance, vertex, neighbour, weight):
                    parent[neighbour] = vertex
                    queue.put( (distance[neighbour], neighbour) )
            #end for 
            done[vertex] = True 
        #end if 
    #end while 
    return distance, parent 
#end procedure ^^^

def shorthestPath(G, a, b):
    distance, parent = Dijkstra(G, a)
    path = []

    while b != None:
        path.append(b)
        b = parent[b] 
    #end while

    path.reverse()
    return path
#end procedure ^^^


graph = [[(1, 20), (2, 30)],
         [(0, 20), (3, 12), (4, 11)],
         [(0, 30), (3, 18), (5, 2700)],
         [(1, 12), (2, 18), (8, 22), ],
         [(1, 11), (6, 15)],
         [(2, 2700), (7, 19), (8, 3)],
         [(4, 15), (8, 8)],
         [(5, 19)],
         [(3, 22), (5, 3), (6, 8)]]

u, v = 0, 7

print( shorthestPath(graph, u, v) ) 