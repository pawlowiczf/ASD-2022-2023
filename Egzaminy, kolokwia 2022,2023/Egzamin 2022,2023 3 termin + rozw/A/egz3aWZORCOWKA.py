from egz3atesty import runtests
from collections import deque

def mapGraph(G):
    #
    n = len(G)
    D = [ [] for _ in range(n) ]

    for vertex in range(n):
       for neighbour in range(n):
          
            if G[vertex][neighbour] != -1:
                D[vertex].append( (neighbour, G[vertex][neighbour] ) )

    #end 'for' loops 

    return D
#end procedure 'mapGraph()'

def BFS(G, s, t):
    #
    n = len(G)

    distance       = [ [ float('inf') for _ in range(17) ] for _ in range(n) ]
    distance[s][0] = 0 

    queue    = deque()
    queue.appendleft( (s, 0, 0) )

    while queue:
        vertex, value, time = queue.popleft()

        if value > 0: queue.append( (vertex, value - 1, time) )
        else:

            for (neighbour, weight) in G[vertex]:

                if distance[vertex][time] + weight + 8 < distance[neighbour][weight]:
                    distance[neighbour][weight] = distance[vertex][time] + weight + 8 
                    queue.append( (neighbour, weight, weight) )

                if time + weight <= 16:
                    if distance[vertex][time] + weight < distance[neighbour][time + weight]:
                        distance[neighbour][time + weight] = distance[vertex][time] + weight 
                        queue.append( (neighbour, weight, time + weight) ) 

            #end 'for' clause 
        #end 'if' clause 
    #end 'while' loop 

    return min( distance[t] )
#end procedure 'BFS()'

def goodknight( G, s, t ):
    #
    D = mapGraph(G)
    return BFS(D, s, t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )