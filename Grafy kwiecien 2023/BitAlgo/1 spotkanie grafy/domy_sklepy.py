"""
Mamy mape miasteczka, w ktorym sa domy i sklepy. Na mapie sa rowniez drogi (kazda dlugosci 1),
ktore lacza dom z domem, albo dom ze sklepem. Dla kazdego domu znajdz odleglosc do najblizszego sklepu.
"""
def addEdge(G, u, v):
    G[u].append(v)
    G[v].append(u)
#


# Wywolujemy BFS, dla kazdego sklepu 

def BFS(G, s, shortestLength):
    n = len(G)
    visited = [ False for _ in range(n) ]
    currLengths = [ 0 for _ in range(n) ]
    #
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        s = queue.pop(0)
        for vertex in G[s]:
            if visited[vertex] == False:
                queue.append( vertex )
                visited[ vertex ] = True 
                currLengths[vertex] += currLengths[s] + 1
                shortestLength[vertex] = min( currLengths[vertex], shortestLength[vertex] )
            #
        #end for
    #end while

#end def ^^^


def Paths(G, shops):
    n = len(G)
    shortestLength = [ float('inf') for _ in range(n) ]
    for shop in shops:
        shortestLength[shop] = 0

    for shop in shops:
        BFS(G, shop, shortestLength)
    #
    return shortestLength

#end def ^^^


shops = [2,4]
V = 8
G = [ [] for _ in range(V) ]

addEdge(G, 0, 1)
addEdge(G, 0, 2)
addEdge(G, 1, 2)
addEdge(G, 2, 3)
addEdge(G, 3, 4)
addEdge(G, 4, 5)
addEdge(G, 5, 6)
addEdge(G, 5, 7)
addEdge(G, 6, 7)

shortestLengths = Paths(G, shops)

for k in range( len( shortestLengths ) ):
    print("Wierzcholek", k, "odleglosc", shortestLengths[k] )