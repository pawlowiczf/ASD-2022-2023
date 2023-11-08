# Algorytm Kahn'a - sortowanie topologiczne

from collections import deque
class Graph:
    indegree = None 

    def __init__(self, edges, n):
        self.adjacencyList = [ [] for _ in range(n) ]
        self.indegree = [ 0 for _ in range(n) ]
    #
        for (source, destination) in edges:
            self.adjacencyList[source].append(destination)
            self.indegree[destination] += 1 
#end class
        
def KahnSorting(G, n):
    #
    
    sortedVertices = []
    indegree = G.indegree 
    S = deque()

    for v in range(n):
        if indegree[v] == 0:
            S.append(v)
    #
    number = len(S)

    while S:
        v = S.pop()
        sortedVertices.append(v)

        for vertex in G.adjacencyList[v]:
            indegree[vertex] -= 1
            if indegree[vertex] == 0: S.append(vertex)
        #end for
        number += 1
    #end while

    # for i in range(n):
    #     if indegree[i]:
    #         return None 
    if number != n:
        return None # jest cykl w grafie
    
    return sortedVertices
#end def ^^^


