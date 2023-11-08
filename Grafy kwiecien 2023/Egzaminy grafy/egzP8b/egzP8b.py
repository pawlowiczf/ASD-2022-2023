from egzP8btesty import runtests

def FloydWarshall(G):
    #
    n = len(G)
    M = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]
    distance = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]

    for vertex in range(n):
        for (neighbour, weight) in G[vertex]:
            M[vertex][neighbour] = weight
            M[neighbour][vertex] = weight
            distance[vertex][neighbour] = weight 
            distance[neighbour][vertex] = weight 
    #end for 

    for v in range(n): 
        M[v][v] = 0
    
    for t in range(n):
        for a in range(n):
            for b in range(n):
                distance[a][b] = min( distance[a][b], distance[a][t] + distance[t][b] )
    #end 'for' loops 

    return distance 

def robot( G, P ):
    #
    n = len(G)
    minCost = 0
    distance = FloydWarshall(G)

    for k in range( len(P) - 1 ):
        #
        vertex, neighbour = P[k], P[k+1]
        minCost += distance[vertex][neighbour]
    #end for
    return minCost 
#end def ^^^


runtests(robot, all_tests = True)
