from zad8testy import runtests

"""
Filip Pawlowicz 414324
Programowanie dynamiczne
Funkcja F(i, a) - minimalna liczba zatrzyman, by dotrzec do pola 'n - 1' z pola 'i', majac na polu 'i' 'a' paliwa.
Sprawdzamy wszystkie potencjalne zasoby paliwa i pola, na ktore mozemy sie wtedy dostac, aktualizujac minimalna liczbe skokow.
O( n^3 )

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

        if 0 <= newY < G.m and 0 <= newX < G.n and not G.visited[newY][newX]:
            if T[newY][newX] > 0:
                G.visited[newY][newX] = True
                amount += DFS(G, T, newY, newX)

    #end 'for' loop 

    return amount 
#end procedure DFS()


def Traverse(T):
    #
    n = len( T[0] )
    F = [ [ float('inf') for _ in range(n + 1) ] for _ in range(n) ]
    C = [ 0 for _ in range(n) ]
    G = Graph(T)

    for energy in range(n + 1):
        F[n - 1][energy] = 0
    #  

    for x in range(n - 1):
        #
        if not G.visited[0][x]: 
            amount = DFS(G, T, 0, x)
            C[x] = amount 
        #
    #end 'for' loop

    for x in reversed( range(n - 1) ):
        for energy in range(n + 1):
            for y in range( x + 1, min( n, x + energy + C[x] + 1 ) ):

                F[x][energy] = min( F[x][energy], F[y][ min(n, energy - (y - x) + C[x] ) ] + 1 )

    #end 'for' loop 

    return F[0][0] 
#end procedure Traverse()


def plan(T):
    #
    return Traverse(T)
#end procedure plan()


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
