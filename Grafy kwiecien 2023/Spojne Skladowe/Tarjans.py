cnt = 0


def DFS(G, n, visited, stack, vertex, minIds, isOnStack, time):
    global cnt
    time += 1
    stack.append(vertex)
    visited[vertex] = time
    minIds[vertex] = time
    isOnStack[vertex] = True

    for neighbour in G[vertex]:

        if visited[neighbour] == -1:
            DFS(G, n, visited, stack, neighbour, minIds, isOnStack, time)
            minIds[ vertex ] = min( minIds[vertex], minIds[neighbour] )

        elif isOnStack[ neighbour ] == True:
            minIds[ vertex ] = min( minIds[vertex], visited[neighbour] )
    #end for 

    if minIds[vertex] == visited[vertex]:
        cnt += 1
        for k in range( len(stack) - 1, -1, -1):

            isOnStack[ stack[k] ] = False 
            minIds[ stack[k] ] = minIds[vertex]
            x = stack.pop()
            print( x , end = " ")

            if x == vertex:
                print()
                break
    #

#end def ^^^

def DfsRun(G, n):
    visited = [ -1 for _ in range(n) ]
    minIds = [ 0 for _ in range(n) ]
    isOnStack = [ False for _ in range(n) ]
    stack = []
    time = 0

    for v in range(n):
        if visited[v] == -1:
            DFS(G, n, visited, stack, v, minIds, isOnStack, time)
    #end for

#end def ^^^


def createG(n, edges):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a = edge[0]
        b = edge[1]
        G[a].append(b)
    #
    return G
#end def ^^^


edges = [ (1, 0), (0, 2), (2, 1), (0, 3), (3, 4) ]
G = createG( 5, edges )
print( DfsRun(G, 5) )
print("------")

edges = [ (0, 1), (3, 0), (2, 3), (1, 2), (2, 4), (4, 5), (5, 6), (6, 4), (6, 7) ]
G = createG( 8, edges )
print( DfsRun(G, 8) )    