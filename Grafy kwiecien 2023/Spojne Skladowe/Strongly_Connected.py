# Algorytm, ktory sprawdza, czy w grafie skierowanym istnieje sciezka miedzy dowolnymi wierzcholkami,
# to znaczy, czy da sie dojsc z wierzcholka a do b oraz z wierzcholka b do a dla dowolnego a i b.
"""
Complete Algorithm:

Start DFS(G, v) from a random vertex v of the graph G. If DFS(G, v) fails to reach every other vertex in the graph G, then there is some vertex u, 
such that there is no directed path from v to u. Thus, G is not strongly connected. If it does reach every vertex, 
then there is a directed path from v to every other vertex in the graph G.
Reverse the direction of all edges in the directed graph G.
Again, run a DFS starting from vertex v. If the DFS fails to reach every vertex, then there is some vertex u, such that in the original graph, 
there is no directed path from u to v. On the other hand, if it does reach every vertex, then there is a directed path from every vertex u to v in the original graph.

If G passes both DFS, it is strongly connected. The algorithm can be implemented as follows in C++, Java, and Python:
"""

class Graph:
    def __init__(self, edges, n):
        self.adjList = [ [] for _ in range(n) ]
        
        for (source, destination) in edges:
            self.adjList[source].append(destination)
        #end for
#end class


def DFS(G, n, visited, v):
    visited[v] = True 

    for vertex in G.adjList[v]:
        if visited[vertex] == False:
            DFS(G, n, visited, vertex)
    #
#end def ^^^

def StrongConnected(G, n):
    visited = [ False for _ in range(n) ]
    DFS(G, n, visited, 0)

    for v in range(n):
        if visited[v] == False:
            return False 
    #
    # Jesli zwroci False, to w pierwszym przejsciu DFS nie udalo sie dojsc do kazdego wierzcholka, wiec nie bylo na pewno sciezki

    # Odwrocenie krawedzi
    edges = []
    for a in range(n):
        for b in G.adjList[a]:
            edges.append( (b, a) )
    #

    newG = Graph(edges, n)
    visited = [ False for _ in range(n) ]
    DFS(newG, n, visited, 0)

    for v in range(n):
        if visited[v] == False:
            return False 
    #

    return True 
#end def ^^^



edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]
n = 5
G = Graph(edges, n)
print( StrongConnected(G, n) )



"""
Input: Graph [edges = [(0, 1), (1, 2), (2, 0)], n = 3]
Output: True

Input: Graph [edges = [(0, 1), (1, 2), (0, 2)], n = 3]
Output: False

Input: Graph [edges = [(0, 1)], n = 2]
Output: False
"""

edges = [(0, 1), (1, 2), (2, 0)]
n = 3
G = Graph(edges, n)
print( StrongConnected(G, n) )

edges = [(0, 1), (1, 2), (0, 2)]
n = 3
G = Graph(edges, n)
print( StrongConnected(G, n) )

edges = [(0, 1)]
n = 3
G = Graph(edges, n)
print( StrongConnected(G, n) )