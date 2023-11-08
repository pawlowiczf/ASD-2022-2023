# Cykl o minimalnej wadze ( wagi krawedzi sa dodatnie )
# Graf nieskierowany, skierowany


"""
Dla grafu skierowanego:

Floyd-Warshall 
Mamy macierz najkrotszych sciezek. Jak z tego wywnioskowac, gdzie mamy cykl o najmniejszej sumie wag?
Kiedy bedziemy wiedziec, czy istnieje cykl? 
Wiaze sie to z domknieciem przechodnim. Czy istnieje polaczenie w obie strony? 
Jesli polaczenie w jedna strone lub w druga nie istnieje, to nie ma cyklu. 
Jesli istnieja takie polaczenie, to suma wag to  waga tego cyklu.
Mozemy teraz sprawdzac kazda pare i zwrocimy cykl o najmniejszej sumie wag. O( N^3 ).

Dla grafu nieskierowanego:

Algorytm Dijkstry
Dla dwoch konkretnych wierzcholkow. 
Uruchamiamy Dijkstre s

# Rozwiazanie dla grafu nieskierowanego znajduje sie w folderze kolokwia grafy w jednym z zadan offline !!!!!!!!!!!!!!!!!!!!!!!
"""

# Dla grafu skierowanego:

def FloydWarshall(G): # G - macierz sasiedztwa, jesli nie ma krawedzi to mamy float('inf')
    #
    n = len(G)
    distance = [ [ float('inf') for _ in range(n) ] for _ in range(n) ] 
    
    for y in range(n):
        for x in range(n):
            if y == x: distance[y][x] = 0 
            else: distance[y][x] = G[y][x] 
    #end for's

    for t in range(n):
        for y in range(n):
            for x in range(n):
                distance[y][x] = min( distance[y][x], distance[y][t] + distance[t][x] )
    #end for's
    return distance

#end procedure FloydWarshall()


def shorthestWeightedCycle(G):
    #
    n = len(G)
    answer = float('inf')
    
    distance = FloydWarshall(G)
    print(distance)

    for a in range(n):
        for b in range(n):
            if a != b: 
                answer = min( answer, distance[a][b] + distance[b][a] )
    #end for's
    
    return answer
#end procedure shorthestWeightedCycle(G)


def createG(edges):
    n = -1 
    for edge in edges:
        a, b, weight = edge
        n = max( n, a, b)
    #
    n += 1
    G = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]
    for edge in edges:
        a, b, weight = edge
        G[a][b] = weight
    #
    return G
#end procedure createG()



    

