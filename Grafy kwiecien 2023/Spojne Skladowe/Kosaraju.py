# Algorytm, ktory wykrywa silnie spojne skladowe w grafie skierowanym
"""
1. Wykonaj DFS na grafie G, posortuj topologicznie  wierzcholki
2. Odwroc kierunek wszystkich krawedzi
3. Ponownie wykonaj DFS, wybierajac startowe wierzcholki od poczatku z sortowania topologicznego


Wierzcholki odwiedzone w danym wykonaniu DFS ( DFS Visit ) tworza silnie spojna skladowa.
"""

from collections import deque

def createG(n, edges):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a = edge[0]
        b = edge[1]
        G[a].append(b)
    #
    return G
#end def ^^^


def addEdge(G, a, b):
    G[a].append(b)
#

def ReverseEdges(G, n):
    newG = [ [] for _ in range(n) ]
    for v in range(n):
        for k in G[v]:
            addEdge(newG, k, v)
    #
    return newG
#


def DFS(G, n, visited, postVisit, source):
    visited[source] = True 

    for vertex in G[source]:
        if visited[vertex] == False:
            DFS(G, n, visited, postVisit, vertex)
    #end for
    postVisit.append(source)

#end def 

def DfsCheck(G, n, visited, source):
    visited[source] = True 
    print(source, end = " ")

    for vertex in G[source]:
        if visited[vertex] == False:
            DfsCheck(G, n, visited, vertex)
    #end for
#end def 


def ConnectedComponents(G, n):
    visited = [ False for _ in range(n) ]
    postVisit = []
    #
    for v in range(n):
        if visited[v] == False:
            DFS(G, n, visited, postVisit, v)
    #

    newG = ReverseEdges(G, n)
    visited = [ False for _ in range(n) ]
    connectedComp = 0 
    
    for v in range( len( postVisit ) - 1, -1, -1):
        if visited[ postVisit[v] ] == False:
            DfsCheck(newG, n, visited, postVisit[v] )
            print()
            connectedComp += 1 
        #
    #end for 
    print()
    return connectedComp
#end def ^^^


edges = [ (1, 0), (0, 2), (2, 1), (0, 3), (3, 4) ]
G = createG( 5, edges )
print( ConnectedComponents(G, 5) )
print("------")

edges = [ (0, 1), (3, 0), (2, 3), (1, 2), (2, 4), (4, 5), (5, 6), (6, 4), (6, 7) ]
G = createG( 8, edges )
print( ConnectedComponents(G, 8) )    