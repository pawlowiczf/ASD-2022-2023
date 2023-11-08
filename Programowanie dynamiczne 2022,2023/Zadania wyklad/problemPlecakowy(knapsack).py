"""
Problem plecakowy (ang. Knapsack) (bez powtorzen)
Dany jest zbior przedmiotow I = {0, 1, 2, ..., n - 1 }
Dla kazdego przedmiotu mamy jego wage i cene, ktore przechowujemy w tablicy
Dana jest takze liczba B - maksymalna waga przedmiotow, ktore mozemy wziac 

Zadanie polega na znalezieniu przedmiotow, ktorych waga nie przekracza B, ale laczna ich cena jest maksymalna.

1) Funkcja do obliczenia:
f(i, b) - maksymalna suma cen przedmiotow ze zbioru {0, 1, 2, ..., n - 1}, ktorych laczna waga nie przekracza b 

2) Sformulowanie rekurencyjne:
f(i, b) = max( f(i-1,b), f( i-1, b - w(i) ) + c(i) ) )

3) Warunki brzegowe:
f(0, b) = c(0), gdy w(0) <= b
f(0, b) = 0, gdy w(0) > b 
"""


def Knapsack(W, C, B): # W - weights, C - cost, B - max weight
    #
    n = len( W )
    F = [ [ 0 for _ in range(B+1) ] for _ in range(n) ]

    for b in range( W[0], B + 1 ):
        F[0][b] = C[0]
    #

    for b in range( B + 1 ):
        for i in range( 1, n ):
            F[i][b] = F[i-1][b]
            if b - W[i] >= 0:
                F[i][b] = max( F[i][b], F[i-1][ b - W[i] ] + C[i] )
    #

    return F[n-1][B], F
#end procedure Knapsack()


# Odtwarzanie zawartosci plecaka (wersja iteracyjna):
def restoreContent(F, W):
    #
    contents = []
    b = len( F[0] ) - 1
    n = len(F)

    # If we have taken an item from the 'i'th row, a profit stored
    # in this row will be different than a profit in a row above

    for i in range( n - 1, 0, -1 ):
        #
        if F[i-1][b] != F[i][b]:
            contents.append(i)
            b -= W[i]

    #end 'for' loop 
    
    # As we will never check the first row in a loop above, we have
    # to asses whether the item from the first row was taken separately
    # We decide to take the first element only if the remaining weight
    # which can be used is no lower than a weight of this element
    if b - W[0] >= 0: contents.append(0)

    contents.reverse()
    return contents
#end procedure restoreContent()



C = [ 60, 100, 120 ]
W = [ 10, 20, 30 ]
B = 50 
profit, F = Knapsack(W, C, B)  # 220 
print(profit)
print( restoreContent(F, W) )
print()

C = [ 83,84,85,76,13,87,2,23,33,82,79,100,88,85,91,78,83,44,4,50,11,68,90,88,73,83,46,16,7,35,76,31,40,49,65,2,18,47,55,38,75,58,86,77,96,94,82,92,10,86,54,49,65,44,77,22,81,52 ]
W = [ 57,95,13,29,1,99,34,77,61,23,24,70,73,88,33,61,43,5,41,63,8,67,20,72,98,59,46,58,64,94,97,70,46,81,42,7,1,52,20,54,81,3,73,78,81,11,41,45,18,94,24,82,9,19,59,48,2,72 ]
B = 41
profit, F = Knapsack(W, C, B) # 414
print(profit)
print( restoreContent(F, W) )
print()

W = [4, 1, 2, 4, 3, 5, 10, 3]
C = [7, 3, 2, 10, 4, 1, 7, 2]
B = 10 
profit, F = Knapsack(W, C, B) # 20
print(profit)
print( restoreContent(F, W) )
print()


W = [5, 3, 4, 2]
C = [60, 50, 70, 30]
B = 5
profit, F = Knapsack(W, C, B) # 80
print(profit)
print( restoreContent(F, W) )
print()

