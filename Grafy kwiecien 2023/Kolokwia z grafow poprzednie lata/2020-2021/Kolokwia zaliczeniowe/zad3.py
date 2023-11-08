from zad3testy import runtests
from queue import PriorityQueue 


def Dijkstra(G, source, destination):
    #
    n = len(G)

    distance  = [ float('inf') for _ in range(n) ]
    graph     = [ [] for _ in range(n) ]

    queue = PriorityQueue()
    queue.put( (0, source) )
    distance[source] = 0 

    while not queue.empty():
        value, vertex = queue.get()

        for (neighbour, weight) in G[vertex]:

            if distance[vertex] + weight < distance[neighbour]:

                distance[neighbour] = distance[vertex] + weight
                queue.put( (distance[neighbour], neighbour) )
                graph[neighbour] = []
                graph[neighbour].append(vertex)
            elif distance[vertex] + weight == distance[neighbour]:
                queue.put( (distance[neighbour], neighbour) )
                graph[neighbour].append(vertex)


        #end for
        
    #end while 
    graph[source] = []
    return graph
#end procedure Dijkstra()


def DFS(G, visited, vertex):
    #
    visited[vertex] = True 
    counter = 0

    for neighbour in G[vertex]:
        if visited[neighbour] == False:
            counter += DFS(G, visited, neighbour)
        counter += 1
    #
    return counter

#end procedure DFS()


def paths(G,s,t):
    #
    n = len(G)
    G = Dijkstra(G, s, t)

    visited = [ False for _ in range( n ) ]
    return DFS(G, visited, t)

#end procedure paths()

    
runtests( paths )


