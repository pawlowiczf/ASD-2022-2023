# Sciezka Hamiltona w grafie DAG
# Zaczynamy od wierzcholka, ktory nie ma krawedzi do niego wchodzacych, czyli jego stopien jest rowny 0
# Sprawdzamy, czy mamy wierzcholek stopnia 0 ( WK )
# idziemy w kolejnosci sortowania topologicznego i patrzymy, czy jest krawedz (v, v+1)

from collections import deque 

def addEdges(G, edges):
    for edge in edges:
        a = edge[0]
        b = edge[1]
        G[a].append(b)
    
#

def DFS(G, path, visited, v):

    visited[v] = True 

    for vertex in G[v]:
        if visited[vertex] == False:
            path = DFS(G, path, visited, vertex)
    #
    path.appendleft(v)
    return path

#end def ^^^    



def SortowanieTopologiczne(G, n):

    visited = [ False for _ in range(n) ]
    path = deque()

    for v in range(n):
        if visited[v] == False:
            path = DFS(G, path, visited, v)
    #
    return path
#end def ^^^

def HamiltonPath(G, n):
    path = SortowanieTopologiczne(G, n)

    for i in range( n - 1 ):
        a = path[i]
        b = path[i+1]
        if b not in G[a]:
            return False
    #
    return True


n = 6
G = [ [] for _ in range(n) ]
edges = [ (0,1), (1, 2), (2, 4), (2, 5), (1, 3) ]
addEdges(G, edges)
print( HamiltonPath(G, n) )

edges = [ (0, 1), (1, 2), (2, 4), (2, 5), (1, 3), (2, 3), (3, 5), (5, 4) ]
G = [ [] for _ in range(n) ]
n = 6
addEdges(G, edges)
print( HamiltonPath(G, n) )

edges = [(1, 0), (1, 2), (1, 3), (3, 0), (2, 3), (2, 5), (3, 5), (0, 4), (4, 5), (5, 6), (4, 6)]
n = 7
G = [ [] for _ in range(n) ]
addEdges(G, edges)
print( HamiltonPath(G, n) )

edges = [(1, 0), (1, 2), (1, 3), (3, 0), (2, 3), (2, 5), (5, 3), (4, 0), (5, 4), (5, 6), (4, 6)]
n = 7
G = [ [] for _ in range(n) ]
addEdges(G, edges)
print( HamiltonPath(G, n) )