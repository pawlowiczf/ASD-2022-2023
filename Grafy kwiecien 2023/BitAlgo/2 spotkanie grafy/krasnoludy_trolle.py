"""
Podziemny labirynt, zlozony z ogromnych jaskin polaczonych waskimi korytarzami. W jednej
z jaskin krasnoludy zbudowaly swoja osade, a w kazdej z pozostalych jaskin mieszka znana
krasnoludom ilosc trolli. Krasnoludy chca zaplanowac swoja obrone na wypadek ataku ze strony trolli.
Zamierzaja w tym celu zakrasc sie i podlozyc ladunek wybuchowy pod jeden z korytarzy tak, aby trolle
mieszkajace za tym korytarzem nie mialy zadnej sciezki, ktora moglyby dotrzec do osady krasnoludow. 

Ktory korytarz nalezy wysadzic w powietrze, aby odciac dostep do krasnoludzkiej osady najwiekszej
liczbie trolli?

Znajdowanie mostow 
"""

# Zakldamy, ze jaskinia krasnoludow jest w wierzcholku 0


def createG(edges, n):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a, b = edge[0], edge[1]
        G[a].append(b)
        G[b].append(a)
    #end for 
    return G
#end procedure createG


def DFS( G, visited, bridges, arrival, vertex, time, parent ):
    #
    time += 1
    visited[vertex] = True 
    arrival[vertex] = time 

    ArrivalTime = time 

    for neighbour in G[vertex]:

        if visited[neighbour] == False:
            ArrivalTime = min( ArrivalTime, DFS(G, visited, bridges, arrival, neighbour, time, vertex) )

        elif neighbour != parent:
            ArrivalTime = min( arrival[vertex], arrival[neighbour] )
    #
    
    if ArrivalTime == arrival[vertex] and parent != -1:
        bridges.append( ( parent, vertex ) )
    #
    return ArrivalTime

#end procedure DFS


def countDwarfs(G, numberOfDwarfs, visited, source):
    visited[source] = True 
    counter = numberOfDwarfs[source]

    for neighbour in G[source]:
        if visited[neighbour] == False:
            counter += countDwarfs(G, numberOfDwarfs, visited, neighbour)
    #
    return counter
#end procedure countDwarfs


def whichDestroy(G, numberOfDwarfs):
    n = len(G)
    bridges = []
    visited = [ False for _ in range(n) ]
    arrival = [ None for _ in range(n)  ]

    DFS(G, visited, bridges, arrival, 0, 0, -1)

    maxOfDwarfs = -1
    whichBridge = None

    for bridge in bridges: # pewne udoskonalenie, to zauwazenie, ze jesli jakis most wystepuje po jakims moscie, to na pewno wysadzenie
        # pierwszego mostu jest lepsza, te pierwsze mosty znajduja sie na koncu tablicy bridges.
        a, b = bridge[0], bridge[1]
        
        visited = [ False for _ in range(n) ]
        visited[a] = True
        counter = countDwarfs(G, numberOfDwarfs, visited, b)

        if counter > maxOfDwarfs:
            maxOfDwarfs = counter 
            whichBridge = (a, b) 
    #end for 
    
    return maxOfDwarfs, whichBridge 
#end procedure whichDestroy 



E = [(0, 1), (1, 2), (2, 0), (3, 1), (3, 0), (4, 3), (5, 3), (5, 7), (5, 6), (6, 7), (0, 8), (8, 9),
     (9, 10), (8, 10), (10, 11), (11, 12), (12, 13), (11, 13)]
C = [0, 2, 8, 1, 7, 3, 5, 4, 3, 1, 2, 4, 5, 2]
G = createG(E, 14)
maxOfDwarfs, whichBridge = whichDestroy(G, C)
print( maxOfDwarfs, whichBridge )


E = [(0, 1), (0, 2), (0, 3), (3, 4), (3, 5), (3, 6)]
C = [0, 5, 5, 4, 2, 2, 1]
G = createG(E, 7)
maxOfDwarfs, whichBridge = whichDestroy(G, C)
print( maxOfDwarfs, whichBridge )


E = [(0, 1), (1, 2), (1, 3), (3, 0), (3, 4), (4, 8), (8, 5), (4, 6), (6, 8), (7, 6)]
C = [0, 2, 7, 13, 5, 2, 3, 1, 5]
G = createG(E, 9)
maxOfDwarfs, whichBridge = whichDestroy(G, C)
print( maxOfDwarfs, whichBridge )


E = [(0, 1), (1, 2), (3, 0), (3, 2)]  # Brak mostów w tym grafie, więc nie opłaca się nic wysadzać
C = [0, 3, 10, 7]
G = createG(E, 4)
maxOfDwarfs, whichBridge = whichDestroy(G, C)
print( maxOfDwarfs, whichBridge )