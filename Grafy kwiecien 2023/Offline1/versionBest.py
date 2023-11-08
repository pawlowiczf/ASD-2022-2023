"""
Algorytm BFS znajduje najkrotsza sciezke miedzy wierzcholkami 's' i 't'. Funkcja edgesInPath dodaje te krawedzie z najkrotszej sciezki do tablicy 'edges' i ja zwraca.
W glownej funkcji 'longer' kazda krawedz z tablicy 'edges' zostaje po kolei usunieta z grafu G (funkcja deleteEdge) i nastepnie zostaje ponownie wywolana funkcja BFS, aby obliczyc dlugosc 
do wierzcholka 't' z wierzcholka 's'. Jesli dlugosc ta ulegla powiekszeniu, to zwracam wierzcholki, ktore tworzyly usunieta krawedz. Jesli nie, dodaje z powrotem te krawedz (funkcja addEdge)
W ten sposob sprawdzimy wszystkie mozliwe przypadki.

+ jesli na poczatku istniala sciezka miedzy wierzcholkami 's' i 't', ale po usunieciu krawedzi z tablicy 'edges' taka sciezka juz nie istnieje,
to odleglosc miedzy wierzcholkami powiekszyla sie i wynosi '+inf'

Zlozonos czasowa O( E(V + E) )
Zlozonosc pamieciowa ( V^3 ) - mozna ja ograniczyc do ( V^2 ) np. uzywajac tablicy 'visited', jako schowka na parent'ow. 
"""


from zad4testy import runtests
from collections import deque 


def deleteEdge(G, a, b):

    for v in range( len( G[b] ) ):
        if G[b][v] == a:
            G[b].pop(v)
            break
    #
    for v in range( len( G[a] ) ):
        if G[a][v] == b:
            G[a].pop(v)
            break

#end def ^^^


def addEdge(G, a, b):
    G[a].append(b)
    G[b].append(a)
#end def ^^^


def BFS(G, s, t):
    n = len(G)
    visited = [ False for _ in range(n) ]
    distance = [ None for _ in range(n) ]
    parent = [ -1 for _ in range(n) ]
    queue = deque()

    visited[s] = True 
    queue.append(s)
    distance[s] = 0


    while queue:
        s = queue.popleft()
        #
        for vertex in G[s]:
            if visited[vertex] == False:

                visited[vertex] = True 
                distance[vertex] = distance[s] + 1
                parent[vertex] = s
                queue.append(vertex)

                if vertex == t: return distance, parent
        #end for
    #end while
    return distance, parent

#end def ^^^


def shortestPath(G, parent, edges, s, t):
    if s != t:
        edges.append( (parent[t], t) )
        shortestPath(G, parent, edges, s, parent[t])

#end def ^^^


def edgesInPath(G, parent, s, t):
    edges = []
    shortestPath(G, parent, edges, s, t)
    return edges 

#end def ^^^


def longer( G, s, t ):
    #
    distance, parent = BFS(G, s, t)
    
    if distance[t] is not None:
        longestPath = distance[t]
    else: return None
    
    edges = edgesInPath(G, parent, s, t)

    for edge in edges:
        a, b = edge[0], edge[1]
        deleteEdge(G, a, b)
        distance, parent = BFS(G, s, t)
        
        if distance[t] != None:
            if distance[t] > longestPath: return (a,b)
        else:
            return (a, b)
        #
        addEdge(G, a, b)
    #end for

    return None
#end def ^^^

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )