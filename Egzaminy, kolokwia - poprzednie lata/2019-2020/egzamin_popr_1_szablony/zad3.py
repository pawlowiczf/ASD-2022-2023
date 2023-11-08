from zad3testy import runtests

def createGraph(T):
    #
    n = len(T)
    G = [ [] for _ in range(n) ]

    for a in range(n):
        for b in range(n):
            if a != b:

                if T[a][b] == 1:
                    G[a].append(b)

                elif T[a][b] == 2:
                    G[b].append(a)

    #end 'for' loops 

    return G
#end procedure createGraph()

def DFS(G, array, visited, vertex):
    #
    visited[vertex] = True 

    for neighbour in G[vertex]:
        if visited[neighbour] == False:
            DFS(G, array, visited, neighbour)
    #

    array.append(vertex)
#end procedure DFS()

def TopologicalSort(G):
    #
    array = [] 
    visited = [ False for _ in range(len(G)) ]

    for vertex in range( len(G) ):
        if visited[vertex] == False:
            DFS(G, array, visited, vertex)
    #

    array.reverse()
    return array 
#end procedure TopologicalSort()

def tasks(T):
    # 
    G = createGraph(T)
    return TopologicalSort(G)
#end procedure tasks()

runtests( tasks )
