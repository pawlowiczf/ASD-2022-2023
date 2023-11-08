# 2 rozwiazania

"""
Topological Sort Algorithm for DAG
Given a Directed Acyclic Graph (DAG), print it in topological order using topological sort algorithm. 
If the graph has more than one topological ordering, output any of them. Assume valid Directed Acyclic Graph (DAG).

A Topological sort or Topological ordering of a directed graph is a linear ordering of its vertices such that 
for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. 
A topological ordering is possible if and only if the graph has no directed cycles, i.e. if the graph is DAG.
"""

def DFS(G, v, visited, departure, time):
    visited[v] = True 
    time = time + 1

    for vertex in G[v]:
        #
        if visited[vertex] == False:
            time = DFS(G, vertex, visited, departure, time)
        #
    #
    departure.append( (v, time + 1) ) 
    return time + 1
#end def ^^^

def DFS_Topological(G, v, visited, departure, time):
    visited[v] = True 
    time = time + 1

    for vertex in G[v]:
        #
        if visited[vertex] == False:
            time = DFS_Topological(G, vertex, visited, departure, time)
        #
    #

    departure[time] = v 
    return time + 1
#end def ^^^


def TopologicalSorting(G):
    n = len(G)
    departure = [ -1 for _ in range( 2 * n ) ]
    visited = [ False for _ in range(n) ]
    time = 0

    for v in range(n):
        if visited[v] == False:
            time = DFS_Topological(G, v, visited, departure, time)
    #
    print(departure)
    for v in range( 2 * n - 1, -1, -1):
        if departure[v] != -1:
            print( departure[v], end = " " )
    #
#end def ^^^


def findDFS(G):
    n = len(G)
    visited = [ False for _ in range(n) ]
    departure = []
    time = 0

    for v in range( n ):
        if visited[v] == False:
            time = DFS(G, v, visited, departure, time)

    departure.sort( key = lambda p: p[1] )

    for v in range( len(departure) - 1, -1, -1 ):
        print( departure[v][0], end = " " )
#end def ^^^

def addEdge(G, edges):
    for edge in edges:
        a, b = edge[0], edge[1]
        G[a].append(b)
#end def ^^^


edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
V = 8
G = [ [] for _ in range(V) ]
addEdge(G, edges)

findDFS(G)
print()
TopologicalSorting(G)
            

