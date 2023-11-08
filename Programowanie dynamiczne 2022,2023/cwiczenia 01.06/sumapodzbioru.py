# Dana jest tablica n liczb naturalnych A. Prosze podac i zaimplementowac
# algorytm, który sprawdza, czy da sie wybrac podciag liczb z A, które sumuja sie do zadanej
# wartosci T.

"""
1) Funkcja F(S, b) = czy istnieje podciag elementow ze zbioru 1, ..., b, ktorego suma jest rowna S
F(S, 0) = False 
F(0, 0) = True 
F(0, b) = True 
Wartosc True jest wtedy, kiedy sposrod elementow 1, ..., b mozna wybrac elementy, ktorych suma jest rowna S 

F(S, b) = F(S, b-1) or F( S - A[b], b - 1 )
Sz: F(T, n)
"""


def subseries(A, T): # A - tablica, T - suma 
    #
    n = len(A)
    F = [ [ False for _ in range(n) ] for _ in range( T + 1 ) ]

    F[0][0] = True 
    for b in range( n ):
        F[0][b] = True 

    for b in range(1, n):
        for S in range(T + 1):

            F[S][b] = F[S][b-1] or F[S][b] 
            if S - A[b] >= 0:
                F[S][b] = F[S][b] or F[ S - A[b] ][ b - 1 ]

    #end 'for' loops 

    return F[T][n-1]
#end procedure subseries()



A = [3, 0, 5, 2, 7, 13, 8]
T = 10
print( subseries(A, T) )
        
A = [3, 5, 2, 7, 13, 8]
T = 6
print( subseries(A, T) )

A = [1, 1, 1, 3, 5, 2, 1, 1, 1, 7, 1, 1, 1, 1, 13, 8]
T = 10
print( subseries(A, T) )
