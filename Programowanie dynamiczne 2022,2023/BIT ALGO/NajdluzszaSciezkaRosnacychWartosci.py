"""
Dana jest tablica (M x N) wypelniona wartosciami. Zadanie polega na znalezieniu najdluzszej
sciezki w tablicy (mozemy przechodzic na pola sasiadujace krawedziami), o rosnacych wartosciach
( tzn. ze z pola o wartosci 3, moge przejsc na pola o o wartosci >= 4 ).

Ulatwienie: dany jest punkt poczatkowy 
"""

def Possible(T, y, x):
    #
    n = len(T)
    m = len( T[0] )

    if 0 <= y < n and 0 <= x < m:
        return True 
    #
    return False 
#end def Possible()


def move(T, F, moves, y, x):
    #
    if F[y][x] == 1:

        for (a, b) in moves:
            newY, newX = y + a, x + b

            if Possible(T, newY, newX) and T[newY][newX] > T[y][x]:
                F[y][x] = max( F[y][x], move(T, F, moves, newY, newX) + 1 )

        #end 'for' loop 
    #end 'if' clause 

    return F[y][x]
#end def move()


def rekMove(T, y, x):
    #
    n = len(T)
    m = len( T[0] )
    moves = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
    F = [ [ 1 for _ in range(m) ] for _ in range(n) ]

    return move(T, F, moves, y, x)
#end procedure rekMove()



"""
Mimo zastosowania podwójnej pętli (złożoność O(n*m) ) oraz wywoływania rekurencji dla każdego punktu, algorytm działa wciąż w czasie 
O(n*m). Wynika to z faktu, iż dla każdego pola, podczas wyznaczania długości ścieżki, od razu wyznaczamy długości wszystkich najdłuższych ścieżek, 
rozpoczynających się w tych polach, które napotykamy po drodze. Zatem dla danego pola tak naprawdę poszukujemy ścieżki tylko raz.
"""

def rekMoveAll(T):
    #
    n = len(T)
    m = len( T[0] )
    moves = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
    F = [ [ 1 for _ in range(m) ] for _ in range(n) ]

    maxLength = -1
    for y in range(n):
        for x in range(m):
            maxLength = max( maxLength, move(T, F, moves, y, x) )
    #

    return maxLength
#end def rekMoveAll()


#end procedure rekMove()
T = [
    [3, 4, 5, 2, 1],
    [7, 2, 13, 7, 8],
    [3, 1, 4, 6, 5],
    [2, 8, 11, 10, 3],
    [3, 5, 1, 6, 2]
]


# y, x = (0, 0)
# print(rekMove(T, y, x)) # 4

# y, x = (3, 0)
# print(rekMove(T, y, x)) # 5

# y, x = (4, 4)
# print(rekMove(T, y, x)) # 6

print( rekMoveAll(T) )