# http://www.graph-magics.com/articles/euler.php
# W przypadku cyklu Eulera w grafie nieskierowanym mozemy zaczac DFS w dowolnym wierzcholku 

from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.n = n
        self.adjacencyList = [ [] for _ in range(n) ]
        self.index = [ 0 for _ in range(n) ] 
        self.parent = [ None for _ in range(n) ]
        self.edge = [ [ 0 for _ in range(n) ] for _ in range(n) ]

        for (source, destination) in edges:
            self.adjacencyList[source].append(destination)
            self.adjacencyList[destination].append(source)
        #
#end class


def DFS2(G, path, vertex):
    #
    if len( G.adjacencyList[vertex] ) % 2 != 0: return None

    for neighbour in G.adjacencyList[ vertex ][ G.index[vertex] : len( G.adjacencyList[vertex] ) ]:
        G.index[vertex] += 1
        if G.edge[vertex][neighbour] == 0 and G.edge[neighbour][vertex] == 0:

            G.edge[vertex][neighbour] = 1
            G.edge[neighbour][vertex] = 1
            path = DFS2(G, path, neighbour)
        #
    #end for 

    if path != None:
        path.appendleft(vertex)
        return path 
    #
    return path
#end def ^^^


def DFS(G, path):
    for v in range( G.n ):
        if len( G.adjacencyList[v] ) > 0:
            path = DFS2(G, path, v)
            break
    #
    return path 
#end def ^^^


edges = [ (0, 1), (1, 4), (3, 4), (3, 2), (4, 0), (4, 2) ]
G = Graph(edges, 5)
path = deque()
path = DFS(G, path)
print(path)

print("-------")

edges = [ (1, 2), (1, 0), (2, 0), (0, 3), (3, 4) ] # nie ma, nie spelnione WKW
G = Graph(edges, 5)
path = deque()
path = DFS(G, path)
print( path )

print("-------")

edges = [ (1, 2), (1, 0), (2, 0), (0, 3), (3, 4), (0, 4) ]
G = Graph(edges, 5)
path = deque()
path = DFS(G, path)
print( path )


print("-------")

edges = [ (1, 2), (1, 3), (1, 0), (2, 0), (0, 3), (3, 4) ] # nie ma, nie spelnione WKW
G = Graph(edges, 5)
path = deque()
path = DFS(G, path)
print( path )

print("-------")

