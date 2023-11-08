def createDirectedG(edges):
    n = 0
    #
    for e in edges:
        a, b = e[0], e[1]
        n = max( n, a, b)
    #
    n += 1
    G = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]
    for edge in edges:
        a, b, weight = edge[0], edge[1], edge[2]
        G[a][b] = weight 
    #
    return G
#end procedure createDirectedG


def FloydWarshall(G):
    # G - graf reprezentowany macierza sasiedztwa 
    n = len(G)
    distance = [ [ 0 for _ in range(n) ] for _ in range(n) ]

    for y in range(n):
        for x in range(n):
            if y == x: distance[y][x] = 0 
            else: distance[y][x] = G[y][x] 
    #end for's
            
    for t in range(n):
        for y in range(n):
            for x in range(n):
                distance[y][x] = min( distance[y][x], distance[y][t] + distance[t][x] )
            #
            # if distance[y][y] < 0: 
            #     print(f"Negative cycle: {y,y}")
            #     return 
    #end for's 
    
    for t in range(n):
        for y in range(n):
            for x in range(n):
                if distance[y][t] + distance[t][x] < distance[y][x]:
                    distance[y][x] = -float('inf')
    #end for's 

    return distance

#end procedure FloydWarshall()


# Testy:

E = [(0, 1, 5), (1, 6, 60), (6, 7, -50), (7, 8, -10), (5, 6, 5), (1, 5, 30), (5, 8, 50), (1, 2, 20),
     (2, 3, 10), (3, 2, -15), (2, 4, 75), (4, 9, 100), (5, 4, 25)]
G = createDirectedG(E)
distance = FloydWarshall(G)
print( distance[0][8] ) # -20 
print( distance[0][9] ) # 160 
print( distance[0][3] ) # 30 

