"""
Oazy i miasta
mamy panstwo

te miasta maja bramy na polnocy i poludniu
miedzy miastami znajduja sie oazy
z miast wychodza drogi na polnoc i poludnie i przechodzi przez jakies oazy 
w reulach panstwa, w przypadku wjazdu do miasta jedna bramu, musimy wyjechac druga
istnie problem, bo mamy czlowieka, ktory chce odwiedzic wszystkie miasta dokladnie raz
jesli goniec wjedzie od polnocy, to musi wyjechac od poludnia 
wyjezdza ze stolicy i wraca do stolicy druga droga. 

narzuca sie ze miasto to krawedz skierowana, w dwie strony, a cala ta przestrzeń ( te krawedzie ) zamienic na wierzcholek
mamy wiec problem znalezienia cykl eulera, a nie cyklu hamiltona. 
nie musza byc jednak krawedzie skierowane 

jak zamienic krawedzie ( te oazy, te duze przestrzenie ) na wierzcholek 


"""

# tablica, ktore wierzcholki to miasta 
# tablica, ktora mowi, ktore miasto odwiedzilismy 

from collections import deque 

def createG(n, edges):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a = edge[0]
        b = edge[1]
        G[a].append(b)
        G[b].append(a)
    #
    return G
#end def ^^^


def DFS(G, cities, visited, visitedCities, v):
    visited[v] = True 

    for neighbour in G[v]:

        if cities[neighbour]:
            visitedCities.append(neighbour)
            visited[neighbour] = True

        elif visited[neighbour] == False:
            DFS(G, cities, visited, visitedCities, neighbour)

    #end for 
#end def ^^^


def createNewGraph(G, cities):

    n = len(G)
    visited = [ False for _ in range(n) ]
    newG = [ [] for _ in range(n) ]
    visitedCities = []


    for v in range(n):

        if visited[v] == False and cities[v] == False:
            DFS(G, cities, visited, visitedCities, v)

            newG[v] = visitedCities
            for k in visitedCities:
                newG[k].append(v)

            visitedCities = []
        #
    #end for
    return newG
#end def ^^^


def OasisAndCities(G, listOfCities):

    n = len(G)
    adjacencyMatrix = [ [ 0 for _ in range(n) ] for _ in range(n) ]
    visited = [ False for _ in range( len(G) ) ]
    cities = [ False for _ in range(n) ]

    for v in listOfCities:
        cities[v] = True 
    #

    G = createNewGraph(G, cities)
    n = len(G)
    print(G)
    for v in range(n):
        if visited[v] == False and cities[v] == False and len( G[v] ) > 0:
            BFS(G, visited, adjacencyMatrix, v)
    #
    newGraph = transformGraph( adjacencyMatrix )
    return newGraph

#end def ^^^


def BFS(G, visited, adjacencyMatrix, vertex):

    queue = deque()
    queue.append(vertex)
    visited[vertex] = True

    while queue:
        s = queue.popleft()

        for neighbour in G[s]:
            adjacencyMatrix[neighbour][s] = 1 

        #end for 
    #end while 

#end def ^^^


def transformGraph( adjMatrix ):
    n = len( adjMatrix )
    G = [ [] for _ in range(n) ]

    for y in range(n):
        a = -1
        b = -1 
        for x in range(n):
            if adjMatrix[y][x] == 1 and a == -1:
                a = x
            elif adjMatrix[y][x] == 1:
                b = x 
        #end fo

        if a != -1 and b != -1:
            G[a].append(b)
            G[b].append(a)
    #end for 
    return G
#end def ^^^

listOfCities = [0, 5, 6, 10]

edges = [ (0, 1), (1, 2), (2, 4), (3, 4), (3, 5), (5, 7), (7, 8), (8, 9), (4, 6), (6, 9), 
         (10, 11), (11, 12), (12, 13), (13, 0), (1, 3), (8, 10) ]


G = createG(14, edges)
newG = OasisAndCities(G, listOfCities)

print( newG )
# na koniec sprawdz cykl Eulera


