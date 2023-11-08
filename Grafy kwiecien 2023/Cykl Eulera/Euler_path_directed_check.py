# Sciezka Eulera w grafie skierowanym
# True/False

""""
A directed graph has an Eulerian path if and only if the following conditions are satisfied:

At most one vertex in the graph has out-degree = 1 + in-degree, and at most one vertex in the graph has in-degree = 1 + out-degree. 
All the remaining vertices have in-degree == out-degree.
All vertices with a non-zero degree belong to a single connected component of the underlying undirected graph. 
In other words, if one removes the “directness” of edges, then the graph without isolated vertices should be connected.

"""
class Graph:
    def __init__(self, edges, n):
        self.adjacencyList = [ [] for _ in range(n) ]
        self.indegree = [ 0 for _ in range(n) ]

        for (source, destination) in edges:
            self.adjacencyList[source].append(destination)
            self.indegree[destination] += 1
#      

def DFS(G, visited, v):
    visited[v] = True 
    for vertex in G.adjacencyList[v]:
        if visited[vertex] == False:
            DFS(G, visited, vertex)
#

def connectedGraph(G, n):
    # czy graf jest spojny?
    visited = [ False for _ in range(n) ]

    # Wykonujemy DFS na wierzcholku, ktory ma wychodzace wierzcholki i sprawdzamy, czy dotrze wszedzie ( do kazdego innego )
    for v in range(n):
        if len( G.adjacencyList[v] ) > 0: 
            DFS(G, visited, v)
            break
    #end for 


    for v in range(n):
        if visited[v] == False and len( G.adjacencyList[v] ) > 0: 
            return False 
    #
    return True 
#end def ^^^

def EulerPath(G, n):
    flagOne = False 
    flagTwo = False 

    for v in range(n):
        outDegree = len( G.adjacencyList[v] )
        inDegree = G.indegree[v]

        if outDegree != inDegree:

            if flagOne == False and inDegree == 1 + outDegree:
                flagOne = True 

            elif flagTwo == False and outDegree == 1 + inDegree:
                flagTwo = True 
            
            else:
                return False 
        #
    #end for 
    return True
#end def ^^^



edges = [(0, 1), (1, 2), (2, 3), (3, 1), (1, 4), (4, 3), (3, 0), (0, 5), (5, 4)]
edges = [ (0, 2), (0, 1), (1, 0), (2, 3), (3, 5), (5, 4), (4, 3) ]


edges = [ (0, 1), (2, 3), (1, 2), (4, 3), (3, 1), (1, 4) ]
G = Graph(edges, 5)
print( EulerPath(G, 5) )
