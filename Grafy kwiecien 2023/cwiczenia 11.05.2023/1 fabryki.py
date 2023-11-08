"""
Mamy dany graf skierowany G = (V,E) oraz funkcje opisujaca
przepustowosc kazdej krawedzi (liczbe jednostek towaru na godzine, które moga sie przemieszczac krawedzia).
Poza tym mamy dany zbiór wierzchołków-fabryk S = {s1, . . . , sn} oraz zbiór wierzchołków-sklepów
T = {t1, . . . , tm}. Dla kazdej fabryki si znamy liczbe pi okreslajaca ile jednostek towaru na godzine fabryka
moze maksymalnie produkowac. Jednoczesnie dla kazdego sklepu tj mamy liczbe qj , która mówi ile jednostek
towaru na godzine musi do tego sklepu docierac. Prosze podac algorytm, który sprawdza, czy da sie
zapewnic, zeby do kazdego sklepu docierało z fabryk dokładnie tyle jednostek towaru ile sklep wymaga jednoczesnie
nie zmuszajac zadnej fabryki do przekroczenia swoich mozliwosci produkcyjnych i nie przekraczajac
przepustowosci zadnej z krawedzi.

"""

"""

Dodaj super wierzcholek zrodlo, dodaj super wierzcholek ujscie, o wagach rownych wagom fabryk, sklepow.
Mamy liste fabryk z krotkami (ilosc produkcji, numer fabryki)
Mamy liste sklepow z krotkami (ilosc towaru, jaka ma dotrzec, number fabryki)

"""

from copy import deepcopy
from collections import deque


def BFS(G, parent, s, t):
    #
    n = len(G)
    visited = [ False for _ in range(n) ]

    queue = deque()
    queue.append( s )
    visited[s] = True 

    while queue:
        #
        vertex = queue.popleft()
        
        for neighbour in range(n):
            if visited[neighbour] == False and G[vertex][neighbour] > 0:
                
                queue.append( neighbour )
                visited[neighbour] = True 
                parent[neighbour]  = vertex

                if neighbour == t: return True
            #end 'if' clause
        #end 'for' loop
    #end 'while' loop

    return False # - nie znaleziono sciezki powiekszajacej do ujscia
#end procedure BFS()


def augmentThePath(G, parent, vertex):
    #
    bottleNeck = float('inf')
    helpVariable = vertex

    while parent[vertex] != None:
        #
        bottleNeck = min( bottleNeck, G[ parent[vertex] ][ vertex ] )
        vertex = parent[vertex]
    #end 'while' loop

    vertex = helpVariable 
    
    while parent[vertex] != None:
        #
        G[ parent[vertex] ][ vertex ] -= bottleNeck
        G[ vertex ][ parent[vertex] ] += bottleNeck 
        vertex = parent[vertex]
    #end 'while' loop 

    return bottleNeck
#end procedure augmentThePath


def FordFulkerson(M, s, t):
    #
    n = len(M)
    maxFlow = 0

    parent = [ None for _ in range(n) ]

    while BFS(M, parent, s, t):
        #
        bottleNeck = augmentThePath(M, parent, t)
        maxFlow += bottleNeck
    #end 'while' loop

    return maxFlow 
#end procedure FordFulkerson


def addExtraVertices(G, factories, shops): # pierwszym element tuple'a jest: (wierzcholek, ilosc produkcji/sprzedazy)
    #
    M = deepcopy(G)
    n = len(M)

    M.append( [ 0 for _ in range( n + 2 ) ] ) # zrodlo, indeks: n
    M.append( [ 0 for _ in range( n + 2 ) ] ) # ujscie, indeks: n + 1

    for y in range( n + 2 ):
        M[y].extend( [0, 0] )
    #end for

    for (vertex, weight) in factories:
        M[n][vertex] = weight 
    
    for (vertex, weight) in shops:
        M[vertex][n+1] = weight 
    #

    return M

#end procedure addExtraVertices()


def fabryki(G, factories, shops):
    #
    M = addExtraVertices(G, factories, shops)
    n = len(M)
    
    s = n - 2 
    t = n - 1

    maxFlow = FordFulkerson(M, s, t)
    print( maxFlow )
    for edge in shops:

        vertex, weight = edge
        if not M[vertex][t] == 0: return False 
    #
    return True 

#end procedure fabryki()



G = [[0, 10, 0, 8, 0, 0, 0],
         [0, 0, 11, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 0],
         [0, 5, 0, 0, 6, 0, 0],
         [0, 0, 0, 0, 0, 0, 12],
         [0, 0, 0, 0, 11, 0, 6],
         [0, 0, 0, 0, 0, 0, 0]]


factories = [(1, 12), (0, 9)]
shops = [(4, 4), (6, 6)]

# printuje tez maxFlow
print( fabryki(G, factories, shops) )