import sys
sys.setrecursionlimit(1000)

class Graph:

    def __init__(self, edges, n):
        self.adjacencyList = [ [] for _ in range(n) ]
        self.indegree = [ 0 for _ in range(n) ]

        for (source, destination) in edges:
            self.adjacencyList[source].append(destination)
            self.indegree[destination] += 1
#end class

def TopologicalSorts(G, path, visited, n):

    for v in range(n):
        if G.indegree[v] == 0 and visited[v] == False:

            for vertex in G.adjacencyList[v]:
                G.indegree[vertex] -= 1
            #
            path.append(v)
            visited[v] = True 

            TopologicalSorts(G, path, visited, n)

            for u in G.adjacencyList[v]:
                    G.indegree[u] += 1
                    
            path.pop()
            visited[v] = False 

    #end for 
    if len(path) == n:
        print(path)
#end def 


def printSorts(G, n):
    path = []
    visited = [ False for _ in range(n) ]
    TopologicalSorts(G, path, visited, n)
#


n = 8
edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
G = Graph(edges, n)

printSorts(G, n)

