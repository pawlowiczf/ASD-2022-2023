
from zad1testy import runtests
from queue import PriorityQueue


def getStations(G, P):
    #
    GasStations = [ False for _ in range( len(G) ) ]

    for station in P:
        GasStations[ station ] = True 
    #end 'for' loop 

    return GasStations
#end procedrure getStations


def Dijkstra(G, P, d, a, b):
    #
    n = len(G)

    distance = [ [ float('inf') for _ in range( d + 1 ) ] for _ in range(n) ]
    parent   = [ [ None for _ in range( d + 1 ) ] for _ in range(n) ]

    queue = PriorityQueue()
    queue.put( (0, a, d) ) # queue.put( (weight, vertex, current fuel) )
    distance[a][d] = 0

    GasStations = getStations(G, P)

    while not queue.empty():
        #
        value, vertex, currentFuel = queue.get()
        fuel = currentFuel

        if vertex == b: return restorePath(parent, b, fuel)

        if GasStations[vertex]:
            currentFuel = d 

        for neighbour in range(n):
            weight = G[vertex][neighbour]

            if weight != -1 and weight <= currentFuel:
                if distance[vertex][fuel] + weight < distance[neighbour][ currentFuel - weight]:
                    
                    distance[neighbour][ currentFuel - weight ] = distance[vertex][fuel] + weight
                    parent[neighbour][ currentFuel - weight ] = (vertex, fuel)
                    queue.put( (distance[neighbour][currentFuel - weight], neighbour, currentFuel - weight) )

        #end 'for' loop 
        
    #end 'while' loop 

    return None
#end procedure Dijkstra()


def restorePath(parent, b, fuel):
    #
    path = []
    pack = (b, fuel)

    while parent[b][fuel] != None:
        path.append(b) 
        b, fuel = parent[b][fuel]  
    #end while  

    path.append(b)
    path.reverse()
    return path

#end procedure restorePath()


def jak_dojade(G, P, d, a, b):
    
    return Dijkstra(G, P, d, a, b)

#end procedure jak_dojade()
        

runtests( jak_dojade ) 

