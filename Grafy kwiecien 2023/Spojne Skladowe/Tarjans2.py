# https://www.baeldung.com/cs/scc-tarjans-algorithm

"""
Tarjan’s algorithm defines arrays \boldsymbol{num[]} and \boldsymbol{lowest[]}, which help in classifying edges. They also help in identifying the starting vertex of an SCC. The algorithm also uses a stack to keep the current DFS tree’s vertices and correctly fetches the vertices of SCCs afterward.

The steps of the algorithm are described below:

Select an unvisited vertex, v. If there’re no unvisited vertices, the algorithm terminates
Run DFS for v
Go to step 1
Inside DFS:

v is marked as visited
num[v] is initialized to be the current value of the counter
lowest[v] is initially equal to num[v]
Next, we go over the v neighbors. If we see an unvisited neighbor, u, we invoke DFS for it and, upon returning, update lowest[v] with lowest[u] if lowest[v] > lowest[u]
If we see a visited but not processed neighbor, w, then we have a back edge. In this case, we update lowest[v] with num[w] if lowest[v] > num[w]
After we process v‘s neighbours, we mark v as processed
After v is processed, we check if num[v] = lowest[v]. If that’s the case, v is the starting vertex of its component. We unwind the stack until we retrieve v. The unwound vertices belong to the  v‘s SCC
"""

class G:
    def __init__(self, n, edges, visited, processed, num, lowest):
        self.counter = 0
        self.n = n
        self.edges = edges
        self.visited = visited
        self.processed = processed
        self.num = num 
        self.lowest = lowest 

        self.adjList = [ [] for _ in range(n) ]

        for (source, destination) in edges:
            self.adjList[source].append(destination)
    #
#end class

def DFS(G, stack, vertex):
    #
    stack.append(vertex)

    G.visited[vertex] = True
    G.num[vertex] = G.counter
    G.lowest[vertex] = G.counter
    G.counter += 1

    for neighbour in G.adjList[ vertex ]:

        if G.visited[neighbour] == False:
            DFS(G, stack, neighbour)
            G.lowest[vertex] = min( G.lowest[vertex], G.lowest[neighbour] )

        elif G.processed[neighbour] == False:
            G.lowest[vertex] = min( G.lowest[vertex], G.num[neighbour] )
    #end for 
    G.processed[vertex] = True 

    if G.lowest[vertex] == G.num[vertex]:
        SCC = []
        k = stack.pop()
        while k != vertex:
            SCC.append(k)
            k = stack.pop()
        #
        SCC.append(k)
        print(SCC)
    #
#end def ^^^

def TARJAN(edges, n):
    #
    visited =   [ False for _ in range(n) ]
    processed = [ False for _ in range(n) ]
    num =       [ 0 for _ in range(n) ]
    lowest =    [ 0 for _ in range(n) ]
    stack = []

    graph = G(n, edges, visited, processed, num, lowest)

    for vertex in range(n):
        if graph.visited[vertex] == False:
            DFS(graph, stack, vertex)
    #end for 
#end def ^^^

edges = [ (1, 0), (0, 2), (2, 1), (0, 3), (3, 4) ]

TARJAN(edges, 5) 
print("------")

edges = [ (0, 1), (3, 0), (2, 3), (1, 2), (2, 4), (4, 5), (5, 6), (6, 4), (6, 7) ]
TARJAN(edges, 8)  
