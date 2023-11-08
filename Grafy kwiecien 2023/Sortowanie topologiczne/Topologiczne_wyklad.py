# Z wykladu
def dfsRecursive(G, vertex, visited, stack):
    visited[vertex] = True 

    for v in G[vertex]:
        if visited[vertex] == False:
            dfsRecursive(G, vertex, visited, stack)
    #
    stack.append(vertex)

#end def ^^^


def DFS(G):
    n = len(G)

    visited = [ False for _ in range(n) ]
    stack = []

    for vertex in range(n):
        if visited[vertex] == False:
            dfsRecursive(G, vertex, visited, stack)
    #

    return stack 
#end def ^^^

def addEdge(G, u, v):
    G[u].append(v)
#

V = 6 
G = [ [] for _ in range(V) ]
addEdge(G, 5, 2)
addEdge(G, 5, 0)
addEdge(G, 4, 0)
addEdge(G, 4, 1)
addEdge(G, 3, 1)
addEdge(G, 2, 3)

stack = DFS(G)
stack = stack[::-1]
print(stack)
