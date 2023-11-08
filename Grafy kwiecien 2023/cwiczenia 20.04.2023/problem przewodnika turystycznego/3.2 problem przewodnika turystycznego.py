"""
Problem polega na znalezieniu ścieżki o maksymalnym wąskim gardle, czyli takiej ścieżki między parą wierzchołków x i y, 
że waga krawędzi o najmniejszej wadze jest największa spośród najmniejszych wag dla wszystkich ścieżek, które łączą x i y. 
Warto zauważyć, że trójki, które dostajemy na wejściu, odpowiadają tak naprawdę ważonym krawędziom skierowanym, z których budujemy graf. 
Do znalezienia ścieżki o najwięszkej przepustowości (zmaksymalizowanym wąskim gardle) 
wykorzystujemy nieco zmodyfikowany algorytm Dijkstry. 
Tym razem nie szukamy najkrótszych ścieżek, ale ścieżek o maksymalnej przepustowości. 
Nie będziemy więc korzystać z kolejki priorytetowej typu minimum, ponieważ chcemy zmaksymalizować przepustowość. 
Konieczne więc będzie wrzucanie do kolejki typu maksimum odpowiedniego wierzchołka wraz z priorytetem równym przepustowości dotychczasowej 
najlepszej ścieżki (ścieżki o największej przepustowości), 
jaka łączy wierzchołek startowy z danym wierzchołkiem. 
Z kolejki zawsze będziemy ściągać ścieżkę o największym wąskim gardle, a więc taką, dla której istnieje największa szansa na uzyskanie maksymalnego przepływu. 
Ponieważ w zadaniu jesteśmy zapytani o znalezienie liczby grup turystów, wystarczy podzielić liczbę wszystkich turystów przez przepustowość wyznaczonej ścieżki
 i wziąć sufit z obliczonej wartości.

 O( ElogV )
"""
from queue import PriorityQueue 
import math 

def createG(edges, n):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a, b, value = edge[0], edge[1], edge[2]
        G[a].append( (b, value) )
        G[b].append( (a, value) )
    #
    return G
#end procedure createG()


def Dijkstra(G, source, destination):
    n = len(G)
    flow   = [ 0 for _ in range(n) ] # przepustowosc
    done   = [ False for _ in range(n) ]
    parent = [ None for _ in range(n) ]

    queue = PriorityQueue() # kolejka priorytetowa typu MAX
    queue.put( (0, source) )
    flow[source] = float('inf')

    while not queue.empty():
        value, vertex = queue.get()

        for (neighbour, weight) in G[vertex]:

            if done[neighbour] == False and neighbour != vertex:
                if weight < flow[vertex]:
                    flow[neighbour] = weight 
                    parent[neighbour] = vertex
                    queue.put( (-1*flow[neighbour], neighbour) )
                elif weight >= flow[vertex]:
                    flow[neighbour] = flow[vertex]
                    parent[neighbour] = vertex
                    queue.put( (-1*flow[neighbour], neighbour) )
        #       
        done[vertex] = True 

        if vertex == destination:
            return flow, parent 
    #end while 
    return flow, parent 
#end procedure Dijkstra()

def GuideProblem(edges, n, K, x ,y):
    #
    G = createG(edges, n)
    flow, parent = Dijkstra(G, x, y)

    minFlow = float('inf')
    while y != None:
        minFlow = min( minFlow, flow[y] )
        y = parent[y]
    #end while 

    return math.ceil( K / minFlow )
#end procedure GuideProblem


edges = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

K = 100
x = 0
y = 3
print( GuideProblem(edges, 13, K, x, y) )

K = 50
x = 0
y = 7
print( GuideProblem(edges, 13, K, x, y) )   


"""
Ciekawy, moze lepszy sposob:


def max_flow_path(G: 'graph represented by adjacency lists',
                  s: 'start vertex',
                  t: 'target vertex'):
    inf = float('inf')
    if s == t: inf
    n = len(G)
    pq = MaxPriorityQueue()
    flows = [0] * n
    flows[s] = inf

    # Insert all the neighbours of the start vertex to a priority
    # queue with a priority which is a weight of an edge from 's' to 'v'
    for v, flow in G[s]:
        pq.insert(flow, v)

    while pq:
        curr_flow, u = pq.poll()

        # Update the max flow value of the 'u' vertex and its parent
        if curr_flow > flows[u]:
            flows[u] = curr_flow
            # Check if a target was reached
            if u == t: break
            # Add all neighbours of the current 'u' vertex that have no
            # max flow path calculated yet to a priority queue
            for v, flow in G[u]:
                if not flows[v]:
                    # Update a path's flow value if the last edge's weight
                    # is lower than a total flow od a path to 'u' vertex
                    pq.insert(min(curr_flow, flow), v)

    return flows[t]

"""