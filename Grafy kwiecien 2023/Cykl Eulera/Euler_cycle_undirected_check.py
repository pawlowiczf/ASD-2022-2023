# Kazdy wierzcholek grafu nieskierowanego musi miec stopien parzysty

class Graph:
    def __init__(self, edges, n):
        self.n = n
        self.adjList = [ [] for _ in range(n) ]

        for (source, destination) in edges:
            self.adjList[source].append(destination)
            self.adjList[destination].append(source)
        #
#end class


def DFS(G, n, visited, vertex, count):
    visited[vertex] = True 

    if len( G.adjList[vertex] ) % 2 == 1:
        return False 
    
    for neighbour in G.adjList[vertex]:
        if visited[vertex] == False:
            if DFS(G, n, visited, neighbour, count):
                return True
    #
    return True

#end def ^^^



def checkEulerCycle(G, n):
    #
    visited = [ False for _ in range(n) ]
    count = 0

    for v in range(n):
        if visited[v] == False:
            if not DFS(G, n, visited, v, count):
                return False 
    #end for 
    return True 
#end def ^^^



edges = [ (0, 1), (1, 4), (3, 4), (3, 2), (4, 0), (4, 2) ]
G = Graph(edges, 5)
print( checkEulerCycle(G, 5) )

print("-------")

edges = [ (1, 2), (1, 0), (2, 0), (0, 3), (3, 4) ] # nie ma, nie spelnione WKW
G = Graph(edges, 5)
print( checkEulerCycle(G, 5) )

print("-------")

edges = [ (1, 2), (1, 0), (2, 0), (0, 3), (3, 4), (0, 4) ]
G = Graph(edges, 5)
print( checkEulerCycle(G, 5) )

print("-------")

edges = [ (1, 2), (1, 3), (1, 0), (2, 0), (0, 3), (3, 4) ] # nie ma, nie spelnione WKW
G = Graph(edges, 5)
print( checkEulerCycle(G, 5) )
print("-------")


