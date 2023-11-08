from copy import deepcopy
# Do dokonczenia: sprawdzenie spojnosci, sprawdzenie, czy stopien kazdego wierzcholka jest parzysty 
def getDegree(G):
    #
    n = len(G)
    degree = [ 0 for _ in range(n) ] 

    for vertex in range(n):
        for neighbour in range(n):
            if G[vertex][neighbour]:

                degree[neighbour] += 1
    #end for's

    return degree
#end procedure Degree()


def DFS(G, n, degree, cycle, vertex):
    #
    for neighbour in range(n):
        if G[vertex][neighbour]:

            G[vertex][neighbour] = 0
            G[neighbour][vertex] = 0
            
            DFS(G, n, degree, cycle, neighbour)
 
    #end for 
    cycle.append(vertex)
    return cycle
#end procedure DFS()


def euler(M):
    #
    n = len(M)
    G = deepcopy(M)

    degree = getDegree(G)

    cycle = []
    cycle = DFS(G, n, degree, cycle, 0)
    cycle.reverse()

    return cycle 
    
#end procedure euler()


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

GG = deepcopy(G)
cycle = euler(G)
print(cycle)

if cycle is None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if not GG[u][v]:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j]:
            print("Błąd (3)!")
            exit(0)

print("OK")
