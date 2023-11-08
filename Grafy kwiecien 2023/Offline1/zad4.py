from zad4testy import runtests

def deleteEdge(G, a, b):

    for v in range( len( G[b] ) ):
        if G[b][v] == a:
            G[b].pop(v)
            break
    #
    for v in range( len( G[a] ) ):
        if G[a][v] == b:
            G[a].pop(v)
            break
    #
#end def ^^^

def addEdge(G, a, b):
    G[a].append(b)
    G[b].append(a)
#
from collections import deque 

def BFS(G, s, t):
    n = len(G)
    visited = [ False for _ in range(n) ]
    distance = [ None for _ in range(n) ]
    parent = [ -1 for _ in range(n) ]
    queue = []

    visited[s] = True 
    queue.append(s)
    distance[s] = 0


    while queue:
        s = queue.pop(0)

        for vertex in G[s]:
            if visited[vertex] == False:

                visited[vertex] = True 
                distance[vertex] = distance[s] + 1
                parent[vertex] = s
                queue.append(vertex)

                if vertex == t: return distance, parent
        #
    #end while
    return distance, parent

#end def ^^^

def shortestPath(G, parent, edges, s, t):
    if s != t:
        edges.append( (parent[t], t) )
        shortestPath(G, parent, edges, s, parent[t])
#end def ^^^

def check(G, parent, s, t):
    edges = []
    shortestPath(G, parent, edges, s, t)
    return edges 
#


def longer( G, s, t ):

    distance, parentEdges = BFS(G, s, t)
    
    if distance[t] is not None:
        longestPath = distance[t]
    else: return None
    
    # edges = check(G, parentEdges, s, t)
    # print(parentEdges)
    # print(edges)

    b = t
    a = parentEdges[t]
    while b != s:
        deleteEdge(G, a, b)
        distance, parent = BFS(G, s, t)
        
        if distance[t] != None:
            if distance[t] > longestPath: return (a,b)
        else:
            return (a, b)
        #
        addEdge(G, a, b)
        b = parentEdges[b]
        a = parentEdges[a]
    #end for

    return None
#end def ^^^

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )