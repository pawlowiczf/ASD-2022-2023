# https://www.baeldung.com/cs/graph-articulation-points
# Uzywajac algorytmu Tarjan'a


class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.visited = [ False for _ in range(n) ]
        self.depth =   [ 0 for _ in range(n) ]
        self.low =     [ 0 for _ in range(n) ]
        self.articulationPoints = []
        self.counter = 0

        self.adjList = [ [] for _ in range(n) ]
        for (source, destination) in edges:
            self.adjList[source].append(destination)
            self.adjList[destination].append(source)
        #
    #end def 
    
#end class


def DFS(G, vertex, parent, root):
    #
    G.visited[vertex] = True 
    G.depth[vertex] = G.counter 
    G.low[vertex] = G.counter
    
    G.counter += 1
    children = 0

    for neighbour in G.adjList[vertex]:
        #
        
        if G.visited[neighbour] == False:
            children += 1
            DFS(G, neighbour, vertex, root)
            G.low[vertex] = min( G.low[vertex], G.low[neighbour] )

            if vertex == root and children > 1:
                G.articulationPoints.append(vertex)

            if G.low[neighbour] >= G.depth[vertex]:
                if vertex != root: # or children > 1, wtedy nie trzeba gornego if'u
                    G.articulationPoints.append(vertex)
        
        elif neighbour != parent:
            G.low[vertex] = min( G.low[vertex], G.depth[neighbour] )
        #                                            

    #end for 

#end def ^^^

def check(G):
    #
    for v in range( G.n ):
        if G.visited[v] == False:
            DFS(G, v, None, v)
    #end for 

    return G.articulationPoints
#end def ^^^


edges = [ (0, 1), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5), (0, 2) ]
G = Graph(6, edges)
vertices = check(G)
print(vertices)

edges = [ (0, 1),(0, 2),(2, 1),(1, 6),(1, 3),(3, 5),(5, 4),(1, 4)]
G = Graph(7, edges)
vertices = check(G)
print(vertices)

edges = [ (1, 0),(0, 2),(2, 1),(0, 3),(3, 4) ]
G = Graph(5, edges)
vertices = check(G)
print(vertices)

edges = [ (0, 1),(1, 2),(2, 3) ]
G = Graph(4, edges)
vertices = check(G)
print(vertices)