# Dla reprezentacji listowej O(EV)

def createGUndirected(edges):
    n = 0
    for edge in edges:
        n = max( n, edge[0], edge[1] )
    #
    G = [ [] for _ in range(n+1) ]
    for edge in edges:
        a, b, weight = edge[0], edge[1], edge[2]
        G[a].append( (b, weight) )
        G[b].append( (a, weight) )
    #
    return G
#end procedure createG()


def createGDirected(edges):
    n = 0
    for edge in edges:
        n = max( n, edge[0], edge[1] )
    #
    G = [ [] for _ in range(n+1) ]
    for edge in edges:
        a, b, weight = edge[0], edge[1], edge[2]
        G[a].append( (b, weight) )
    #
    return G
#end procedure createG()


def shorthestPath(parent, distance, source, destination):
    if distance[destination] == -float('inf'): return None # brak sciezki, cykl ujemny 

    path = []
    while destination != None:
        path.append(destination)
        destination = parent[destination]
    #
    path.reverse()
    return path 
#end procedure shorthestPath()


def relax(distance, a, b, weight):
    if distance[b] > distance[a] + weight:
        distance[b] = distance[a] + weight 
        return True 
    #
    return False 
#end procedure relax()


def BellmanFord(G, source):
    #
    n = len(G)
    distance = [ float('inf') for _ in range(n) ]
    distance[source] = 0

    for _ in range(n-1):
        for a in range(n):
            for (b, weight) in G[a]:
                k = relax(distance, a, b, weight)
        #
    #

    # Poszukiwanie ujemnego cyklu
    for _ in range(n-1):
        for a in range(n):
            for (b, weight) in G[a]:
                if relax(distance, a, b, weight):
                    distance[b] = -float('inf')
        #
    #
    return distance
#end procedure BellmanFord()


E = [(0, 1, 5), (1, 6, 60), (6, 7, -50), (7, 8, -10), (5, 6, 5), (1, 5, 30), (5, 8, 50), (1, 2, 20),
     (2, 3, 10), (3, 2, -15), (2, 4, 75), (4, 9, 100), (5, 4, 25)]
s = 0

G = createGDirected(E)
print( BellmanFord(G, s) )

# Dla grafu nieskierowanego możemy iść w dowolną stronę, więc zawsze wejdziemy w ujemny cykl
G = createGUndirected(E)
print( BellmanFord(G, s) )

print(" --------------------- " )

# Dla reprezentacji macierzowej O(V^3)