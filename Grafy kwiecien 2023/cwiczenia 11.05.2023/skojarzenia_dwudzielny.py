# Skojarzenia w grafach dwudzielnych
"""
W grafie dwudzielnym mozna podzielic wierzcholki na dwa zbiory, przy czym krawedzie wystepuja tylko miedzy
wierzcholkami z osobnych zbiorow.

Skojarzenie - zbior krawedzi, ze zadne dwie krawedzie nie maja wspolnego elementu (wierzcholka)


Najliczniejsze skojarzenie znajdujemy przez obliczenie maksymalnego przeplywu
Dodaj sztuczne wierzcholki - zrodlo, ujscie, polacz odpowiednio te zbiory.
Kazda krawedz ma pojemnosc 1

O(V^3) 

https://youtu.be/GhjwOiJ4SqU
Hungarian algorithm
"""
from collections import deque 
from copy import deepcopy

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


def createVertices(Graph):
    # tworzymy nowe jedno zrodlo i nowe jedno ujscie

    # Reprezentacja: graf Edmondsa: M - osoby, N - zadania. Stworz graf w postaci macierzowej rozmiaru: M + N + 2 
    n = len( Graph[0] ) # ilosc zadan
    m = len( Graph ) # ilosc osob 
    size = n + m + 2

    G = [ [ 0 for _ in range( n + m + 2 ) ] for _ in range( n + m + 2 ) ]

    for guy in range(m):
        #
        G[ size - 2 ][ guy ] = 1

        for machine in range(n):
            if Graph[guy][machine] == 1:
                G[ guy ][ m + machine ] = 1 
    #end for 

    for machine in range(n):
        G[ m + machine ][ size - 1 ] = 1
    #end for 

    return FordFulkerson(G, size - 2, size - 1)
#end procedure createVertices


def MaximumBipartiteMatching(G):
    
    return createVertices(G)
#end procedure()



G = [ [0, 1, 1, 0, 0, 0],
[1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1] ]

print( MaximumBipartiteMatching(G) )

G = [ [0, 1, 0, 0, 1],
[0, 0, 1, 0, 0],
[0, 1, 1, 1, 1],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 0, 1, 1] ]

print( MaximumBipartiteMatching(G) )