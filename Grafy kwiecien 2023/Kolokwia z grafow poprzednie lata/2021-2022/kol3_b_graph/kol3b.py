from kol3btesty import runtests
from queue import PriorityQueue


def airports( G, A, s, t ):
    #
    n = len(G)

    processed = [ False for _ in range(n+1) ]
    distance  = [ float('inf') for _ in range(n+1) ]
    G.append( [] )

    for v in range(n):
        G[n].append( (v, A[v]) )
        G[v].append( (n, A[v]) )

    queue = PriorityQueue()
    queue.put( (0, s) ) # queue.put( (value, vertex) )
    distance[s] = 0

    while not queue.empty():
        #
        value, vertex = queue.get()
        processed[vertex] = True

        if value == distance[vertex]:

            for (neighbour, weight) in G[vertex]:
                
                if processed[neighbour] == False and distance[vertex] + weight < distance[neighbour]:
                    distance[neighbour] = distance[vertex] + weight
                    queue.put( ( distance[neighbour], neighbour) )
                #end if's

        if vertex == t:
            return distance[t]
            #end for's
    #end while
    return distance[t]
#end procedure airports()


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )