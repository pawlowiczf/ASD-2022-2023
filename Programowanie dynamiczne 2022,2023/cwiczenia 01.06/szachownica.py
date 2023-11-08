# Dana jest szachownica A o wymiarach n × n. Szachownica
# zawiera liczby wymierne. Nalezy przejsc z pola (1, 1) na pole (n,n) korzystajac jedynie z ruchów “w dół”
# oraz “w prawo”. Wejscie na dane pole kosztuje tyle, co znajdujaca sie tam liczba. Prosze podac algorytm
# znajdujacy trase o minimalnym koszcie.

"""
print( *T, sep = '\n' )
"""

def chessboard(T, F, dict, y, x):
    #

    if y == 0 and x == 0: return T[y][x] 
    #
    if y < 0 or x < 0: return float('inf')

    if not (y, x) in dict: 
        dict[ (y,x) ] = T[y][x] + min( chessboard(T, F, dict, y - 1, x), chessboard(T, F, dict, y, x - 1) )
        F[y][x] = dict[ (y,x) ]

    return F[y][x]
#end procedure chessboard


def TopDown(T, F, n, y, x):
    #
    if y == n - 1 and x == n - 1:
        F[y][x] = T[y][x] 
        return F[y][x]
    #
    if x >= n or y >= n: return float('inf')

    if F[y][x] == float('inf'):
        F[y][x] = min( TopDown(T, F, n, y, x + 1), TopDown(T, F, n, y + 1, x) ) + T[y][x] 
    #

    return F[y][x]
#end procedure TopDown()

"""
Bez rekurencji. 
Funkcja F, ktora wyznacza koszt dotarcia do pola (y, x)
Tablica F[y][x] bedzie oznaczala, jaki byl koszt dotarcia do danego pola 

W podejściu bottom-up wypełniamy tablicę od początkowego do końcowego punktu (odwrotnie niż w top-down). 
Najpierw zauważamy, że w pierwszym wierszu oraz w pierwszej kolumnie możemy się poruszać tylko w obrębie tego wiersza/kolumny 
(tzn. nie da się wejść do pierwszego wiersza z wiersza wyżej, bo takiego nie ma, więc poruszamy się po nim tylko w prawo; 
analogicznie dla 1. kolumny). Zatem najpierw wypałniamy pierwszy wiersz oraz pierwszą kolumnę wartościami (kosztami przejścia na dane pole), 
a następnie przechodzimy do wypełniania pozostałej części tablicy pomocniczej, decydując dla każdego pola, czy lepiej do niego wejść z lewej strony 
(idąc w stronę prawą), czy z góry (idąc w dół) i zapisujemy minimalny koszt dostania się do tego pola.

F[y][x] = T[y][x], gdy y == x ==0
F[y][x] = min( F[y-1][x] + T[y][x] , F[y][x-1] + T[y][x] ),, dla 
"""

def BottomUp(T):
    #
    n = len(T)
    F = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]

    F[0][0] = T[0][0]

    for x in range(1, n):
        F[0][x] = F[0][x-1] + T[0][x] 
    #

    for y in range(1, n):
        F[y][0] = F[y-1][0] + T[y][0]
    #

    for y in range(1, n):
        for x in range(1, n):
            F[y][x] = min( F[y-1][x] , F[y][x-1] ) + T[y][x]
    #end 'for' loops 

    return F[n-1][n-1] 
#end procedure chess(T)


from random import randint
n = 100
T = [ [ randint(1,30) for _ in range(n) ] for _ in range(n) ]

dict = {}
F = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]
print( chessboard(T, F, dict, n - 1, n - 1) )

F = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]
print( TopDown(T, F, n, 0, 0) )

print( BottomUp(T) )










