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
    distance = [ [ 0 for _ in range(n)    ] for _ in range(n) ]
    parent =   [ [ None for _ in range(n) ] for _ in range(n) ]

    for y in range(n):
        for x in range(n):
            if y == x: distance[y][x] = 0 
            else: 
                distance[y][x] = G[y][x] 
                parent[y][x] = y
    #end for's
            
    for t in range(n):
        for y in range(n):
            for x in range(n):
                if distance[y][t] + distance[t][x] < distance[y][x]:
                    distance[y][x] = distance[y][t] + distance[t][x] 
                    parent[y][x] = parent[t][x]
                
            #
    #end for's 
    
    for t in range(n):
        for y in range(n):
            for x in range(n):
                if distance[y][t] + distance[t][x] < distance[y][x]:
                    distance[y][x] = -float('inf')
                    parent[y][x] = -1
    #end for's 

    return distance, parent 

#end procedure FloydWarshall()

def shorthestPath(parent, a, b, path):
    if b == a:
        return 
    shorthestPath(parent, a, parent[a][b], path)
    path.append(b)
#end procedure shorthestPath()

def paths(G, a, b):
    distance, parent = FloydWarshall(G)
    path = [a]
    if parent[a][b] == -1 and a != b: return None 
    shorthestPath(parent, a, b, path)

    path.reverse()
    return path
#end procedure paths()


E = [(0, 1, 5), (1, 6, 60), (6, 7, -50), (7, 8, -10), (5, 6, 5), (1, 5, 30), (5, 8, 50), (1, 2, 20),
     (2, 3, 10), (3, 2, -15), (2, 4, 75), (4, 9, 100), (5, 4, 25)]
G = createDirectedG(E)
distance, parent = FloydWarshall(G)
print( distance[0][8] ) # -20 
print( paths(G, 0, 8)  )
print("----")

print( distance[0][9] ) # 160 
print( paths(G, 0, 9)  )
print("----")

print( distance[0][3] ) # 30 
print( paths(G, 0, 3)  )
print("----")

print( distance[1][7] ) #  
print( paths(G, 1, 7)  )
print("----")