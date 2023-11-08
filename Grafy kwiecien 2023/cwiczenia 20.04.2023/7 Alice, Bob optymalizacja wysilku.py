""""
Dana jest mapa kraju w postaci grafu G = (V,E), gdzie wierzchołki to
miasta a krawedzie to drogi łaczace miasta. Dla kazdej drogi znana jest jej długosc (wyrazona w kilometrach
jako liczba naturalna). Alicja i Bob prowadza (na zmiane) autobus z miasta x > V do miasta y > V , zamieniajac
sie za kierownica w kazdym kolejnym miescie. Alicja wybiera trase oraz decyduje, kto prowadzi pierwszy.
Prosze zapropnowac algorytm, który wskazuje taka trase (oraz osobe, która ma prowadzic pierwsza), zeby
Alicja przejechała jak najmniej kilometrów.


Optymalizacja wysilku tylko jednego kierowcy



2. Dla kazdego miasta mamy 2 opcje, albo wyjedzie z niego ALice albo Bob, skoro tak
to byc moze chcemy rozmnocy wierzcholki, dla kazdego miasta bedziemy miec 2 wierzcholki,
to teraz rozmnazamy krawedzie, ale madrze. Mielismy np. krawedz o wadze 57, teraz bedziemy miec dwie krawedzie o wadze 57, ktora
oznacza ze Alice przejedzie 57 kilometrow, oraz krawedz o wadze 0, ktora Bob przejedzie. Musi byc tak,
zeby te krawedzie wystepowaly na zmiane. Chcielibysmy, moze zeby te krawedzie byly skierowane.
W ten sposob przerabiamy graf ,ale jeszcze na poczatku i na koncu, musimy umozliwic wybor 
wyszukujemy najkrotsza sciezke 4 razy miedzy wierzcholkiem A1B1, A1B2, A2B1, A2B2/
albo dodajemy 2 wierzcholki jeszcze A' B' z dwoma wychodzacymi krawedziami. 

3. ALbo na kolejke wrzucamy Dijkstry najkrotsza sciezke jaka do tej pory przejechalismy oraz inforomacje,
czy prowadzila Alice, czy Bob. Jesli do miasta dojechalismy Alice, to wrzucamy sasiadow , ale ze jedzie tam Bob
ale wrzucamy te sama odleglosc x dojazdu. 
"""

from queue import PriorityQueue 

def shorthestPath(parent, source, destination):
    path = []
    while destination != None:
        path.append(destination)
        destination = parent[destination]
    #
    path.reverse()
    return path
#end procedure shorthestPath


def createGWeight(edges, n):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a, b, weight = edge[0], edge[1], edge[2]
        G[a].append( (b, weight) )
        # G[b].append( (a, weight) )
    #
    return G
#end procedure createGWeight


def Dijkstra(G, source, destination, whoStarts):
    n = len(G)

    distance = [ float('inf') for _ in range(n) ]
    parent   = [ None for _ in range(n)         ]
    done     = [ False for _ in range(n)        ]

    queue = PriorityQueue()
    queue.put( (0, source, whoStarts) )
    distance[source] = 0

    while not queue.empty():
        value, vertex, whoDroveBefore = queue.get()
        #
        for (neighbour, weight) in G[vertex]:
            if done[neighbour] == False:
                #
                if whoDroveBefore == 'Alice':
                    distance[neighbour] = distance[vertex]
                    queue.put( ( distance[neighbour], neighbour, "Bob" ) )
                    parent[neighbour] = vertex
                
                elif whoDroveBefore == 'Bob':
                    if distance[neighbour] > distance[vertex] + weight:
                        distance[neighbour] = distance[vertex] + weight 
                        parent[neighbour] = vertex
                        queue.put( ( distance[neighbour], neighbour, "Alice" ) )
                #end if's
        #end for 
        done[vertex] = True 
        if vertex == destination:
            return distance, parent

    #end while
    return distance, parent
#end procedure Dijsktra 
    


edges = [ (0, 3, 70), (0, 1, 100), (1, 2, 15), (1, 7, 33), (2, 8, 2), (2, 4, 15), (4, 5, 11), (5, 9, 1), (5, 6, 98), (9, 6, 47),
          (6, 10, 30), (7, 9, 63), (7, 8, 6), (0, 2, 54), (4, 8, 50), (3, 4, 20) ]

edges = [ (0, 3, 10), (0, 1, 100), (1, 2, 15), (1, 7, 33), (2, 8, 2), (2, 4, 15), (4, 5, 100), (5, 9, 1), (5, 6, 98), (9, 6, 47),
          (6, 10, 30), (7, 9, 63), (7, 8, 6), (0, 2, 54), (4, 8, 50), (3, 4, 100) ]

G = createGWeight(edges, 11)

distance, parent = Dijkstra(G, 0, 10, "Bob") # startuje Alice
print( shorthestPath(parent, 0, 10) )
print( distance[10] )

distance, parent = Dijkstra(G, 0, 10, "Alice") # startuje Bob
print( shorthestPath(parent, 0, 10) )
print( distance[10] )

print(" --------------------------------------- ")

edges= [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

G = createGWeight(edges, 13)

distance, parent = Dijkstra(G, 0, 7, "Bob") # startuje Alice
print( shorthestPath(parent, 0, 7) )
print( distance[7] )

distance, parent = Dijkstra(G, 0, 7, "Alice") # startuje Bob
print( shorthestPath(parent, 0, 7) )
print( distance[7])

print(" --------------------------------------- ")

distance, parent = Dijkstra(G, 0, 5, "Bob") # startuje Alice
print( shorthestPath(parent, 0, 5) )
print( distance[5] )

distance, parent = Dijkstra(G, 0, 5, "Alice") # startuje Bob
print( shorthestPath(parent, 0, 5) )
print( distance[5])

print(" --------------------------------------- ")

distance, parent = Dijkstra(G, 0, 11, "Bob") # startuje Alice
print( shorthestPath(parent, 0, 11) )
print( distance[11] )

distance, parent = Dijkstra(G, 0, 11, "Alice") # startuje Bob
print( shorthestPath(parent, 0, 11) )
print( distance[11])

print(" --------------------------------------- ")

distance, parent = Dijkstra(G, 0, 8, "Bob") # startuje Alice
print( shorthestPath(parent, 0, 8) )
print( distance[8] )

distance, parent = Dijkstra(G, 0, 8, "Alice") # startuje Bob
print( shorthestPath(parent, 0, 8) )
print( distance[8])


print(" --------------------------------------- ")

distance, parent = Dijkstra(G, 9, 2, "Bob") # startuje Alice
print( shorthestPath(parent, 9, 2) )
print( distance[2] )

distance, parent = Dijkstra(G, 9, 2, "Alice") # startuje Bob
print( shorthestPath(parent, 9, 2) )
print( distance[2])
