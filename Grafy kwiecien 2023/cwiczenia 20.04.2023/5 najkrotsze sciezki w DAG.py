# Najkrotsze sciezki w DAG wazonym od wierzcholka do wszystkich pozostalych
# Sortowanie topologiczne O(E)
"""
Uruchomienie jednej iteracji Bernalla Forda 

"""

def DFS(G, visited, sortedArray, v):
    #
    visited[v] = True 
    for (neighbour, value) in G[v]:
        if visited[neighbour] == False:
            DFS(G, visited, sortedArray, neighbour)
    #end for 

    sortedArray.append(v)
#end procedure DFS


def sortedTopological(G, n):
    visited = [ False for _ in range(n) ]
    sortedArray = []

    for v in range(n):
        if visited[v] == False:
            DFS(G, visited, sortedArray, v)
    #end for 
    return sortedArray
#end procedure sortedTopological


def shorthestPathDAG(G, n, source):
    #
    distance = [ float('inf') for _ in range(n) ]
    parent   = [ None for _ in range(n) ]
    
    sortedArray = sortedTopological(G, n)
    sortedArray.reverse()

    distance[source] = 0

    for v in sortedArray[ sortedArray.index(source) : len( sortedArray ) ]:
        for ( neighbour, weight ) in G[v]:
            if distance[neighbour] > distance[v] + weight:
                distance[neighbour] = distance[v] + weight 
                parent[neighbour] = v 
    #
    return distance, parent
#end def ^^^



def createG(edges, n):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a, b, value  = edge[0], edge[1], edge[2]
        G[a].append( (b, value) )
    #
    return G
#end procedure createG


edges = [ (0, 3, 5), (2, 3, 6), (2, 1, 4), (2, 0, 3), (1, 4, 1), (4, 5, 10), (4, 7, 2), (7, 6, 9), (6, 5, 8), (0, 1, 4) ]
G = createG(edges, 8)
print(G)
distance, parent = shorthestPathDAG(G, 8, 0)

for v in range(1, 8):
    print(f"Odleglosc do wierzcholka {v} to: {distance[v]}")
