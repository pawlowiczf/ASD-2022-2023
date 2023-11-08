"""
Do znalezienia najwiekszego, mozliwego dopasowania pracownikow do maszyn uzylem algorytmu Hopcrofta-Karpa. 
Algorytm ten dziala w czasie O( V^5/2 ), wiec jest szybszy od naiwnej implementacji algorytmu Forda-Fulkersona, w ktorym to, w pierwotnej wersji, budowalem graf rozmiaru 2n+2. 
Dziala natomiast na podobnej zasadzie, tj. dopoki istnieja sciezki powiekszajace, to wyszukuje je. 

Jednakze, sciezki te musza spelniac okreslone warunki:

- dowolne 2 sciezki nie moga zawierac tego samego wierzcholka (vertex-disjoint set)
- sciezka musi naprzemian zawierac krawedzie niedopasowane oraz dopasowane, to znaczy idac ze zbioru U do V musi isc
krawedzia, ktora nie nalezy do zadnego dopasowania, ale idac ze zbioru V do U musi isc krawedzia juz dopasowana.
- sciezka zaczyna sie w wierzcholku niedopasowanym w zbiorze U i konczy sie w wierzcholku niedopasowanym w zbiorze V ( w tym celu uzywany jest tzw. dummy Vertex, w moim przypadku wierzcholek o indeksie n )

Sciezki sa wyszukiwane algorytmem BFS. Natomiast algorytm DFS zamienia stan kazdej krawedzi nalezacej do danej sciezki.
Jesli krawedz danej sciezki byla juz dopasowana, to zostaje "usunieta z dopasowania", a krawedz, ktora nie byla dopasowana
zostaje odpowiednio dopasowana. Zauwazmy, ze w ten sposob, dla kazdej sciezki powiekszajacej, ilosc naszych dopasowan zawsze wzrasta o 1, 
gdyz zaczelismy od krawedzi niedopasowanej i naprzemian dopasowana, niedopasowana... 
Z jednej dopasowanej, dwoch niedopasowanych, po zamianie stanow, dostalismy dwie dopasowane, jedna niedopasowana itd.


O( V^5/2 )
"""
from zad6testy import runtests
from collections import deque 


class Graph:

    def __init__(self, adjList, n):

        self.n       = n
        self.pairU   = [ n for _ in range( n ) ] # dopasowania pracownikow do maszyn 
        self.pairV   = [ n for _ in range( n ) ] # dopasowania maszyn do pracownikow 
        self.adjList = adjList 

    #end def 
#end Class 


def BFS(G, distance):
    #
    queue = deque ()
    n = G.n

    for vertex in range(n):
        if G.pairU[ vertex ] == n:
            
            distance[ vertex ] = 0 
            queue.append( vertex )
        else:
            distance[vertex] = float('inf')
    #end for 
    distance[n] = float('inf')

    while queue:

        vertex = queue.popleft()

        if vertex != n:
            for neighbour in G.adjList[ vertex ]:
                if distance[ G.pairV[ neighbour ] ] == float('inf'):

                    queue.append( G.pairV[ neighbour ] )
                    distance[ G.pairV[ neighbour ] ] = distance[ vertex ] + 1 

                #end 'if' clause     
            #end 'for' loop 
        #end 'if' clause 

    #end 'while' loop 

    return distance[n] != float('inf')
#end procedure BFS()


def FindPath(G, distance, vertex):
    #
    n = G.n
    parent = [ None for _ in range(n+1) ]
    dummyVertex = n

    queue = deque()
    queue.append( vertex ) # queue.put( ( its ancestor from left side, its ancestor from right side ) )

    while queue:
        vertex = queue.pop()

        if vertex == dummyVertex: return parent 

        for neighbour in G.adjList[ vertex ]:

            if distance[ G.pairV[neighbour] ] == distance[ vertex ] + 1:
                queue.append( G.pairV[neighbour] )
                parent[ G.pairV[neighbour] ] = ( vertex, neighbour )
            #end 'if' clause 

        #end 'for' loop 
    #end 'while' loop 

    return False 
#end procedure FindPath()


def changeCondition(G, parent):
    #
    vertex = G.n 
    vertex, ancestor = parent[vertex]

    while parent[vertex] != None:
        G.pairU[vertex]   = ancestor 
        G.pairV[ancestor] = vertex 
        vertex, ancestor = parent[vertex]
    #end while 
    G.pairU[vertex]   = ancestor 
    G.pairV[ancestor] = vertex 

#end procedure changeCondition()
    


def binworker( M ):
    #
    n = len(M)
    G = Graph( M, n )

    matching = 0
    distance = [ float('inf') for _ in range( G.n + 1 ) ]

    while BFS(G, distance):
        #
        for vertex in range( G.n ):
            if G.pairU[ vertex ] == G.n:
                parent = FindPath(G, distance, vertex)
                if parent:
                    changeCondition(G, parent)
                    matching += 1 
        #end 'for' loop 
    #end 'while' loop 

    return matching 
#end procedure binworker()


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )
