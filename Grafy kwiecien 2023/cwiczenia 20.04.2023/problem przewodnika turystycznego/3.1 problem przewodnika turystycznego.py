# Problem przewodnika turystycznego
# Kazda krawedz ma wage, ktora przechowuje informacje o tym, jaka jest pojemnosc kazdego autobusu
# W kazdym wierzcholku trzymamy informacje o tym, ile grup potrzeba aby do niego dojsc
# Macierz sasiedztwa ale na krawedzie 

"""
Wez wszystkie krawedzie i je posortuj po pojemnosci autobusow 
nastepnie jedna po drugiej dodawaj je do grafu dopoki nie zacznie istniec ta sciezka ( find union )

lub wyszukiwanie binarne 

czy istnieje krawedz aby przewiezc 2 grupy (100 uczestnikow)? wyrzucamy wszystkie krawedzie o wadze mniejszej niz 50.


1)
- robimy BFS, ale jak dojdziemy do krawedzi i jest taka sobie, to moze najptymalniej isc gdzie indziej, 
taki bfs, ze w kazdym wierzcholku trzymamy informacje, jaka jest minimalna waga krawedzi (czyli najmniejsza pojemnosc autobousow)
mamy tez visited (macierz) na krawedzie
aktualizujemy zawsze jak najptymalniej mozemy dojsc do danego wierzcholka 

2)
po kolei dodajemy wierzcholki w kolejnosci malejacych wag i w ktorym momencie mozemy dojsc do konca, waga ostatniej krawedzi jaka dodalismy
to jest ta minimalna pojemnosc autobusu

Puszczamy grupke ta sama sciezka, ale tak, zeby poscic tych grup jak najmniej 
Posortuj krawedzie malejaco
Rob mst, fragment tego mst wykorzystaj 
maksymalne drzewo rozpinajace 
do kolejki wrzucaj wagi z minusami, wtedy dostaniesz najwieksze drzewo rozpianajace 
"""

from collections import deque
import math

def createGraph(edges, n):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a = edge[0]
        b = edge[1]
        G[a].append(b)
        G[b].append(a)
    #
#

def addEdge(G, a, b):
    G[a].append(b)
    G[b].append(a)
#


def BFS(G, n, source, destination):
    visited = [ False for _ in range(n) ] 
    queue = deque()

    visited[source] = True 
    queue.append(source)

    while queue:
        s = queue.popleft()

        for vertex in G[s]:
            if visited[vertex] == False:
                visited[vertex] = True 
                queue.append(vertex)
            
                if vertex == destination:
                    return visited
            #
        #
    #end while

    return visited
#end def ^^^


def getVertices(edges):
    maxVertex = 0
    for edge in edges:
        a = edge[0]
        b = edge[1]
        maxVertex = max( maxVertex, a )
        maxVertex = max( maxVertex, b)
    #
    return maxVertex + 1
#end def ^^^


def TouristGuide(K, edges, A, B):
    #
    n = getVertices(edges)
    edges.sort( key = lambda x: x[2], reverse = True )
    print(edges)
    numberGroups = 0

    G = [ [] for _ in range(n) ]

    for edge in edges:
        #
        a = edge[0]
        b = edge[1] 
        value = edge[2]

        addEdge(G, a, b)
        # numberGroups = max( numberGroups, math.ceil( K / value) )

        visited = BFS(G, n, A, B)
        if visited[B] == True: return math.ceil( K / value ) # return numberGroups
    #end for 

#end def ^^^

edges = [
    (0, 1, 50),
    (0, 3, 25),
    (1, 2, 75),
    (2, 3, 20),
    (3, 5, 50),
    (5, 6, 2),
    (4, 6, 10),
    (6, 7, 20),
    (7, 8, 70),
    (1, 5, 75),
    (2, 5, 30),
    (3, 4, 50)
]


print( TouristGuide(100, edges, 0, 8) )


        
