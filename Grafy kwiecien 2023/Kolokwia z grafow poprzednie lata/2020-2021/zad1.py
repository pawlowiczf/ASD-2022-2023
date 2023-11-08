from zad1testy import runtests
from math import inf


def FloydWarshall(G):
    #
    n = len(G)
    distance = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]


    # Edytowanie tablicy 'distance'

    for y in range(n):
        for x in range(n):

            if y == x: distance[y][x] = 0 
            elif G[y][x] != 0: distance[y][x] = G[y][x]
    #end for's


    # Wykonanie algorytmu 'Floyda-Warshalla'

    for t in range(n):
        for y in range(n):
            for x in range(n):
                distance[y][x] = min( distance[y][x], distance[y][t] + distance[t][x] )
    #end for's

    return distance
#end procedure FloydWarshall()


def findPossiblePaths(M, d, distance):
    #
    n = len(M)
    G = [ [ [] for _ in range(n) ] for _ in range(n) ]

    for y1 in range(n):   
        for x1 in range(n):
            
            if d <= distance[y1][x1]:

                for y2 in range(n):
                    for x2 in range(n):

                        if y1 != x2 or y2 != x1: # nie moga isc w przeciwne strony przez krawedz jednoczesnie 
                        
                            if ( y1 == y2 ) and ( x1 != x2 ) and M[ y1 ][ y2 ] == 0 and M[ x1 ][ x2 ] > 0: 
                                if d <= distance[ y2 ][ x2 ]:
                                    G[ y1 ][ x1 ].append( (y2, x2) )

                            if ( y1 != y2 ) and ( x1 == x2 ) and M[ y1 ][ y2 ] > 0 and M[ x1 ][ x2 ] == 0: 
                                if d <= distance[ y2 ][ x2 ]:
                                    G[ y1 ][ x1 ].append( (y2, x2) )

                            if ( y1 != y2 ) and ( x1 != x2 ) and M[ y1 ][ y2 ] > 0 and M[ x1 ][ x2 ] > 0: 
                                if d <= distance[ y2 ][ x2 ]:
                                    G[ y1 ][ x1 ].append( (y2, x2) )
                            

                #end for's 3,4
    #end for's 1, 2

    return G
#end procedure findPossiblePaths()


def DFS(G, visited, parent, source, destination, x, y):
    #
    visited[x][y] = True 

    if x == destination and y == source:
        return True 
    
    for (a, b) in G[x][y]:

        if visited[a][b] == False:
            parent[a][b] = (x, y)
            
            if DFS(G, visited, parent, source, destination, a, b):
                return True 
    #end for

    return False 

#end procedure DFS()


# def trackThePath( parent, coords ):
#     path = []

#     while coords:
#         path.append(coords)
#         u, v = coords
#         coords = parent[u][v]
#     #end while 

#     path.reverse()
#     return path

# #end procedure trackThePath

def trackThePath( parent, y, x ):
    path = []

    while parent[y][x] != None:
        path.append( (y, x) )
        y, x = parent[y][x]
    #end while 

    path.append( (y, x) )
    path.reverse()

    return path

#end procedure trackThePath


def keep_distance(M, x, y, d):
    #
    n = len(M)

    distance = FloydWarshall(M)
    G = findPossiblePaths(M, d, distance)

    visited = [ [ False for _ in range(n) ] for _ in range(n) ]
    parent  = [ [ None for _ in range(n) ] for _ in range(n) ]

    DFS(G, visited, parent, x, y, x, y)

    #return trackThePath( parent, (y, x) )
    return trackThePath( parent, x, y )

#end procedore keep_distance()

runtests( keep_distance )

# Inne rozwiazanie, taka sama zlozonosc obliczeniowa, ale pamieciowa tylko V^2:

"""
def floyd_warshall(G: 'graph represented by adjacency matrix'):
    n = len(G)
    inf = float('inf')
    W = [[inf] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j]:
                W[i][j] = G[i][j]
            elif i == j:
                W[i][j] = 0

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = W[i][t] + W[t][j]

    return W


def get_path(parents, coords):
    path = []

    while coords:
        path.append(coords)
        u, v = coords
        coords = parents[u][v]

    path.reverse()
    return path


def keep_distance(M, x, y, d):
    dist = floyd_warshall(M)
    G = create_graph(M, dist, d)
    n = len(G)
    inf = float('inf')

    visited = [[False] * n for _ in range(n)]
    parents = [[None] * n for _ in range(n)]

    def dfs(u, v):
        visited[u][v] = True
        if u == y and v == x:
            return True
        
        for u2 in range(n):
            if u2 != u and not M[u][u2]: continue
            for v2 in range(n):
                if visited[u2][v2] or \
                    (v2 != v and not M[v][v2]) or \
                    (u == u2 and v == v2) or \
                    (u2 == v and v2 == u): 
                    continue
                if d <= dist[u2][v2] < inf:
                    parents[u2][v2] = u, v
                    dfs(u2, v2)
        return False

    dfs(x, y)

    return get_path(parents, (y, x))
"""