"""
Dostajemy na wejsciu liste krawedzi drzewa (niekoniecznie binarnego) oraz wyrozniony
wierzcholek - korzen. Kazdy wierzcholek tworzy wlasne poddrzewo. Dla kazdego wierzcholka, wyznacz
ilosc wierzcholkow w jego poddrzewie
"""
# Graf skierowany, drzewo:

def addEdge(G, v, u):
    G[v].append(u)


def DFS(G, v, visited):
    if G[v] == []:
        visited[v] = 1
    else:
        visited[v] = 1
        for vertex in G[v]:
            DFS(G, vertex, visited)
            visited[v] += visited[vertex]
    #
#end def ^^^


def CountVertices(G, v):
    n = len(G)
    visited = [ 0 for _ in range(n) ]
    DFS(G, v, visited)
    #
    return visited
#end def ^^^


V = 10
G = [ [] for _ in range(V) ]

addEdge(G, 0, 1)
addEdge(G, 0, 2)
addEdge(G, 0, 3)
addEdge(G, 1, 4)
addEdge(G, 1, 5)
addEdge(G, 3, 6)
addEdge(G, 3, 7)
addEdge(G, 3, 8)
addEdge(G, 3, 9)


visited = CountVertices(G, 0)

for vertex in range(V):
    print( "Wierzcholek", vertex, "ma dzieci: ", visited[vertex] )