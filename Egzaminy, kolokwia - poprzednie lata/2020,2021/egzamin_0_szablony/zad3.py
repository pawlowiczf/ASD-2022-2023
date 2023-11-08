from zad3testy import runtests
from queue import PriorityQueue

def Dijkstra(G, s, t):
    #
    n = len(G)

    distance = [ [ float('inf') for _ in range(2) ] for _ in range(n) ] 
    distance[s][0] = 0 

    queue = PriorityQueue()
    queue.put( (0, (0, s) ) )

    # queue.put( value, (state, vertex) ), gdzie state: 0 - doszedlem do wierzcholka nie wykorzystujac butow, 1 - doszedlem wykorzystujac buty 

    while not queue.empty():
        value, (state, vertex) = queue.get()
        if vertex == t: return distance[t][state]

        if state == 0: 

            for a in range(n):
                if G[vertex][a] and vertex != a:

                    for b in range(n):
                        if G[a][b]:

                            edgeValue = max( G[vertex][a], G[a][b] )

                            if distance[vertex][0] + edgeValue < distance[b][1]:
                                distance[b][1] = distance[vertex][0] + edgeValue
                                queue.put( (distance[b][1], (1, b) ) )

                    #end for
            #end for 
        #end 'if' clause

        for a in range(n):
            
            if G[vertex][a]:
                if distance[vertex][0] + G[vertex][a] < distance[a][0]:
                    distance[a][0] = distance[vertex][0] + G[vertex][a] 
                    queue.put( (distance[a][0], (0, a) ) )

                if distance[vertex][1] + G[vertex][a] < distance[a][0]:
                    distance[a][0] = distance[vertex][1] + G[vertex][a]
                    queue.put( (distance[a][0], (0, a) ) )
        #

    #end while
    return min( distance[t][0], distance[t][1] )
def jumper(G, s, t):
    #
    return Dijkstra(G, s, t)
#end procedure jumper()

runtests(jumper)
