"""
Funkcja F(y, x): (N, N) --> (N, N) 
Dwuargumentowa funkcja, dwuargumentowa przeciwdziedzina 

Funkcja zwraca liste (pseudo krotka): 
    - pierwsza wartosc w 'krotce': maksymalna liczba komnat mozliwa do odwiedzenia po przyjsciu od lewej lub gory
    - druga wartosc w 'krotce':    maksymalna liczba komnat mozliwa do odwiedzenia po przyjsciu od lewej lub dolu

W algorytmie przechodze od gory do dolu i wypelniam w ten sposob tablice F. Jesli ide z gory na dol (kolumna ta sama) to aktualizuje
wartosc na pierwszej pozycji w krotce, jesli ide od dolu w gore, to aktualizuje druga pozycje w krotce.
Natomiast aktualizujac, sprawdzam obie wartosci z lewej i po jednej z gory lub z dolu, w zaleznosci, w ktora strone sie poruszam

Warunki brzegowe: 
    - do pol z pierwszej kolumny moge dostac sie tylko idac z gory, wiec aktualizuje tylko pierwsza wartosc w krotce 
    - do pol z pierwszego wiersza moge dostac sie tez tylko z lewej, ale zgodnie z przyjeta zasada, aktualizuje obie wartosci


"""

from zad7testy import runtests


def FillObjectives(L, F, n):
    #
    for y in range(n):
        for x in range(n):

            if L[y][x] == '#':
                F[y][x] = [ -float('inf'), -float('inf') ]
            #

    #end 'for' loops 

    return F 
#end procedure FillObjectives()


def Traverse( L ):
    #
    n = len(L)

    F = [ [ [0, 0] for _ in range(n) ] for _ in range(n) ]
    F = FillObjectives(L, F, n)

    # Pierwsza wartosc w 'krotce': maksymalna liczba komnat mozliwa do odwiedzenia po przyjsciu od lewej lub gory
    # Druga wartosc w 'krotce':    maksymalna liczba komnat mozliwa do odwiedzenia po przyjsciu od lewej lub dolu

    # Warunki brzegowe:

    for row in range(1, n):
        F[row][0][0] += F[row - 1][0][0] + 1
        F[row][0][1] =  -float('inf')
    #

    for column in range(1, n):
        F[0][column][0] += F[0][column - 1][0] + 1
        F[0][column][1] += F[0][column - 1][1] + 1
    #

    # Dynamiczne wypelnianie tablicy F:

    for x in range(1, n): # kolumna ----------------------------------

        if L[0][x] == '.':
            F[0][x][0] = max( F[0][x - 1][0], F[0][x - 1][1] ) + 1

        for y in range(1, n): # wiersz

            leftMaxValue = max( F[y][x - 1][0], F[y][x - 1][1] )
            upMaxValue   = F[y - 1][x][0]
            
            if L[y][x] == '.':
                F[y][x][0] = max( leftMaxValue, upMaxValue) + 1
            #
        #end 'for' loop 

        if L[n - 1][x] == '.':
            F[n - 1][x][1] = max( F[y][x - 1][0], F[y][x - 1][1] ) + 1

        for y in reversed( range(n - 1) ): # range: <2, n - 2>, ale odwrotna kolejnosc

            leftMaxValue = max( F[y][x - 1][0], F[y][x - 1][1] )
            downMaxValue = F[y + 1][x][1]

            if L[y][x] == '.':
                F[y][x][1] = max( leftMaxValue, downMaxValue ) + 1
            #
        #end 'for' loop 

    #end 'for' loop -------------------------------------------------

    return F[n - 1][n - 1][0] if F[n - 1][n - 1] != [ -float('inf'), -float('inf') ] else -1
#end procedure Traverse()



def maze( L ):
    #
    return Traverse( L )
#end procedure maze()


runtests( maze, all_tests = True )