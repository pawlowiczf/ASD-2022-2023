"""
Pewien podróznik chce przebyc trase z punktu A
do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy.Wbaku miesci
sie dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawedzie to
łaczace je drogi. Kazda krawedz ma długosc w kilometrach (przedstawiona jako licza naturalna). W kazdym
wierzchołku jest stacja benzynowa, z dana cena za litr paliwa. Prosze podac algorytm znajdujacy trase z
punktu A do punktu B o najmniejszym koszcie.

"""

"""
W skrócie to idea jest taka, że korzystamy z algorytmu Dijkstry (jak praktycznie zawsze, gdy chodzi o 
najkrótsze/najtańsze ścieżki z wagami nieujemnymi), ale musimy nieco zmienić sposób relaksacji wierzchołków. 
Tym razem do wierzchołka możemy dotrzeć z różną ilością paliwa, 
więc pierwsze dotarcie najtańszą dotychcas ścieżką może się okazać 
niewystarczające z tego względu, że np. zabraknie nam paliwa, by jechać dalej. 
Jest jeszcze jeden problem, a mianowicie, wjeżdżając na stację, nie wiemy, ile na niej musimy zatankować i jaki jest koszt tankowania. 
z tego powodu najtańsza dotychczas ścieżka może stać się nieopłacalna. Konieczne jest zatem myślenie o wierzchołkach jak o serii 
 D + 1 wierzchołków ( 0 <= i <= D ), gdzie dotarcie do danego wierzchołka 
 oznacza przyjechanie na stację z ilością paliwa w postaci i litrów. Konieczne jest więc 
wyznaczanie najkrótszych ścieżek do wierzchołków (stacji) przy danej ilości końcowej paliwa. 

"""

from queue import PriorityQueue

def Dijkstra(G, petrolStationsCost, capacityOfFuel, currentAmountFuel, source, destination):
    #
    n = len(G)
    cost   = [ [ float('inf') for _ in range( capacityOfFuel + 1 ) ] for _ in range(n) ]

    cost[0][currentAmountFuel] = 0

    queue = PriorityQueue()

    # queue.put[ minValue, amountOfFuel, vertex ]
    queue.put( (0, currentAmountFuel, source) ) # minValue - najmniejszy koszt dotarcia do wierzcholka v ( tj. koszt tankowania )

    while not queue.empty():
        value, amountOfFuel, vertex = queue.get()

        for (neighbour, weight) in G[vertex]:
            for d in range( 0, capacityOfFuel - amountOfFuel + 1 ):
                    
                    if weight <= d + amountOfFuel and cost[vertex][amountOfFuel] + d * petrolStationsCost[vertex] < cost[neighbour][ d + amountOfFuel - weight ]:
                    
                        cost[neighbour][ d + amountOfFuel - weight ] = cost[vertex][amountOfFuel] + d * petrolStationsCost[vertex]
                        queue.put( ( cost[vertex][amountOfFuel] + d * petrolStationsCost[vertex], d + amountOfFuel - weight, neighbour ) )
                    #end if
            #end for 2
        #end for 1
        if vertex == destination:
            return cost
    #end while 
    return cost
    
#end procedure Dijkstra()

def costOfTravel(G, petrolStationsCost, currentAmountFuel, capacityOfFuel, source, destination):
    cost = Dijkstra(G, petrolStationsCost, capacityOfFuel, currentAmountFuel, source, destination)
    

    minCost = float('inf')
    for v in cost[destination]:
        if v < minCost: minCost = v 
    #
    if minCost != float('inf'): return minCost
    return None
#end procedure costOfTravel()


def createG(edges, n):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a, b, weight = edge[0], edge[1], edge[2]
        G[a].append( (b, weight) )
        G[b].append( (a, weight) )
    #
    return G
#end procedure createG()


E = [(0, 1, 5), (1, 2, 3), (0, 2, 7), (2, 3, 4), (3, 4, 6)]
C = [8, 5, 3, 2, 1]
G = createG(E, 5)

s = 0
t = 4
capacity = 10
fuel = 0
print( costOfTravel(G, C, fuel, capacity, s, t) )


E = [(0, 1, 4), (0, 7, 5), (0, 6, 8), (6, 7, 3), (1, 6, 6), (7, 8, 20), (8, 4, 9),
     (5, 6, 12), (5, 4, 7), (1, 2, 15), (5, 2, 17), (2, 4, 10), (2, 3, 5), (4, 3, 18)]
C = [5, 7, 3, 5, 2, 1, 8, 10, 6]
G = createG(E, 9)

s = 0
t = 3
capacity = 14
fuel = 5
print( costOfTravel(G, C, fuel, capacity, s, t) )