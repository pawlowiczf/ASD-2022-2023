from queue import PriorityQueue


def relax(distance, vertex, neighbour, weight):
    #

    if distance[vertex] + weight < distance[neighbour]:
        return True 
    return False 

#end procedure relax()


def Dijkstra(G, source):
    #
    n = len(G)
    distance = [ float('inf') for _ in range(n) ]
    parent   = [ None for _ in range(n)         ]
    done     = [ False for _ in range(n)        ]

    queue = PriorityQueue()
    queue.put( (0, source) )
    distance[source] = 0
    done[source] = True 
    
    while not queue.empty():
        value, vertex = queue.get()

        for neighbour in range(n):
            if G[vertex][neighbour] > 0 and relax( distance, vertex, neighbour, G[vertex][neighbour] ):
                distance[neighbour] = distance[vertex] + G[vertex][neighbour]
                queue.put( (distance[neighbour], neighbour) )
                parent[neighbour] = vertex 
        #end for
        done[vertex] = True 
    #end while 
    return distance 


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
  

distance = Dijkstra(graph, 0)

print( distance )