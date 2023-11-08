class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.visited = [ False for _ in range(n) ]
        self.depth =   [ 0 for _ in range(n) ]
        self.low =     [ 0 for _ in range(n) ]
        self.bridges = []
        self.counter = 0

        self.adjList = [ [] for _ in range(n) ]
        for (source, destination) in edges:
            self.adjList[source].append(destination)
            self.adjList[destination].append(source)
        #
    #end def 
    
#end class


def DFS(G, root, vertex, parent):
    #
    G.visited[vertex] = True 
    G.depth[vertex]   = G.counter 
    G.low[vertex]     = G.counter 

    G.counter += 1

    for neighbour in G.adjList[vertex]:

        if G.visited[neighbour] == False:
            DFS(G, root, neighbour, vertex)
            G.low[vertex] = min( G.low[vertex], G.low[neighbour] )
        
        elif parent != neighbour:
            G.low[vertex] = min( G.low[vertex], G.depth[neighbour] )

        # ----------

        if G.low[neighbour] > G.depth[vertex]:
            G.bridges.append( (vertex, neighbour) )
        
    #end for 

#end procedure DFS()
    


edges = [ (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5) ]
G = Graph(6, edges)
DFS(G, 0, 0, None)
print( G.bridges )



E = [(0, 1), (1, 2), (2, 0), (3, 1), (3, 0), (4, 3), (5, 3), (5, 7), (5, 6), (6, 7), (0, 8), (8, 9),
     (9, 10), (8, 10), (10, 11), (11, 12), (12, 13), (11, 13)]

G = Graph(14, E)
DFS(G, 0, 0, None)
print( G.bridges )


