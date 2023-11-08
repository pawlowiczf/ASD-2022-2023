from zad8testy import runtests
from queue import PriorityQueue

"""
Filip Pawlowicz 414324
Podejscie zachlanne 
Z pola na ktorym jestem, patrze na pola, na ktorem moge isc i dodaje do kolejki priorytetowej wartosci zloz paliwa.
Z kolejki wybieram zloze o najwiekszej pojemnosci i ide na najdalsze pole, na ktore pozwala mi aktualna ilosc paliwa.
W ten sposob nie sprawdzamy wszystkich mozliwych zatrzyman, ale je 'omijamy'. 
Wybieramy zawsze najdalsza pozycje, na ktora mozemy isc, wiec jesli rozwiazanie istnieje, to znajdziemy optymalne.

"""

class Graph:
    def __init__(self, T):
        self.n = len( T[0] )
        self.m = len( T )
        self.visited = [ [ False for _ in range( self.n ) ] for _ in range( self.m ) ] 
        self.moves   = [ (1, 0), (0, -1), (-1, 0), (0, 1) ]
#end class 


def DFS(G, T, y, x):
    #
    G.visited[y][x] = True 
    amount = T[y][x]
    T[y][x] = 0

    for (a, b) in G.moves:
        newY, newX = y + a, x + b

        if 0 <= newY < G.m and 0 <= newX < G.n and G.visited[newY][newX] == False:
            if T[newY][newX] > 0:
                amount += DFS(G, T, newY, newX)

    #end 'for' loop 

    return amount 
#end procedure DFS()


def Traverse(T):
    #
    n = len( T[0] )

    C = [ 0 for _ in range(n) ]
    G = Graph(T)

    jumps = 0

    for x in range(n):
        #
        if not G.visited[0][x] and T[0][x] > 0: 
            amount = DFS(G, T, 0, x)
            C[x] = amount 
        #
    #end 'for' loop

    x = 0
    fuel = 0

    while x < n - 1:
        #
        queue = PriorityQueue()
        for y in range( x + 1 ):
            if C[y] > 0:
                queue.put( (-C[y], y) )
        #

        jumps += 1 
        fuel, index = queue.get()
        C[index] = 0

        fuel *= -1 
        x += fuel

    #end 'while' loop 

    return jumps 
#end procedure Traverse()


def plan(T):
    #
    return Traverse(T)
#end procedure plan()


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
