from zad1testy import runtests
from queue import PriorityQueue

def Dijkstra(G, A, B):
    #
    n = len(G)

    # 0 - przylecialem, 1 - przyplynalem, 2 - doszedlem 
    cost = [8, 5, 1]
    distanceCost = [ [ float('inf') for _ in range(3) ] for _ in range(n) ]

    distanceCost[A][0] = 0 
    distanceCost[A][1] = 0
    distanceCost[A][2] = 0

    queue = PriorityQueue()
    queue.put( (0, (0, A) ) )
    queue.put( (0, (1, A) ) )
    queue.put( (0, (2, A) ) )

    while not queue.empty():
        #
        value, (state, vertex) = queue.get() 
        if vertex == B: return distanceCost[B][state]

        for neighbour in range(n):
            for way in range(3):

                if way != state and G[vertex][neighbour] > 0:

                    if distanceCost[vertex][state] + G[vertex][neighbour] < distanceCost[neighbour][way]:
                        distanceCost[neighbour][way] = distanceCost[vertex][state] + G[vertex][neighbour]
                        queue.put( (distanceCost[neighbour][way], (way, neighbour)) )

                #end 'if' clauses
        #end 'for' loops 
    #
    return None
#end procedure Dijkstra()


def islands(G, A, B):
    # 
    return Dijkstra(G, A, B)
#end procedure islands()
        
runtests( islands ) 
