"""
Do znajdowania najkrotszych sciezek w grafie wazonym wykorzystalem algorytm Dijkstry. Algorytm Dijkstry wykorzystuje kolejke priorytetowa, wierzcholek z najmniejsza
dotad odlegloscia od wierzcholka startowego jest wyciagany z kolejki, a nastepnie nastepuje relaksacja jego sasiadow.

Grafy w poblizu osobliwosci tworza tak naprawde jeden wierzcholek tzn. mozna sobie wyobrazic, ze tworza one pewien zbior, w ktorym odleglosci od elementow 
zbioru sa rowne 0. Taki zbior utozsamiam z jednym wierzcholkiem. Jesli wierzcholek startowy lub koncowy lub oba sa osobliwosciami, to wtedy sa tym nowo-utworzonym
wierzcholkiem. 

Powyzsze usprawnienie powoduje, ze nie musimy dodawac do grafu wszystkich osobliwosci, dodajemy tylko jeden wierzcholek (ktory utozsamiamy ze zbiorem osobliwosci),
ktory jest polaczony z odpowiednimi wierzcholkami-nie osobliwosciami. Dzieki temu uzyskujemy zlozonosc algorytmu, taka sama, jaka jest zlozonosc Algorytmu Dijkstry,
tj. ElogV

O(ElogV)
zlozonosc pamieciowa O( V^3 ) + wielkosc kolejki priorytetowej 
"""



from zad5testy import runtests
from queue import PriorityQueue


def Singularity(n, S):
    isSingularity = [False for _ in range(n)]
    for v in S:
        isSingularity[v] = True
    #
    return isSingularity

# end procedure Singularity


def createG(n, E, isSingularity):
    G = [[] for _ in range(n + 1)]

    for edge in E:
        a, b, value = edge

        if isSingularity[a] == True and isSingularity[b] == False:
            G[n].append((b, value))
            G[b].append((n, value))

        elif isSingularity[a] == False and isSingularity[b] == True:
            G[n].append((a, value))
            G[a].append((n, value))

        elif isSingularity[a] == False and isSingularity[b] == False:
            G[a].append((b, value))
            G[b].append((a, value))
    # end for
    return G

# end procedure createG


def Dijkstra(G, n, source, destination):

    distance = [float('inf') for _ in range(n)]
    done = [False for _ in range(n)]

    queue = PriorityQueue()
    distance[source] = 0
    queue.put((0, source))

    while not queue.empty():
        value, vertex = queue.get()

        for (neighbour, weight) in G[vertex]:

            if done[neighbour] == False and ( distance[vertex] + weight ) < distance[neighbour]:

                distance[neighbour] = distance[vertex] + weight
                queue.put((distance[neighbour], neighbour))
            #
        # end for
        done[vertex] = True

        if vertex == destination:
            return distance
    #end while

    return distance

#end procedure Dijkstra


def spacetravel(n, E, S, a, b):
    #
    isSingularity = Singularity(n, S)
    G = createG(n, E, isSingularity)
    #
    if isSingularity[a] and isSingularity[b]: 
        return 0
    if isSingularity[a]:
        a = n
    if isSingularity[b]:
        b = n
    #
    distance = Dijkstra(G, n + 1, a, b)
    #
    
    if distance[b] == float('inf'):
        return None
    return distance[b]

# end procedure spacetravel

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
