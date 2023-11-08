# Posortuj tablice T[n] takich liczb 0 <= T_i <= n^2 - 1
# O(n)
# Co-pilot
"""
Zamien liczby na system o podstawie n
Uzywamy Radix Sorta, 
O(n)
"""

def change(x, n, i): # x - liczba, n - podstawa systemu, i - pozycja
    if i == 1:
        return x % n
    return ( x // n ) % n

#end def ^^^

def countingSort(T, n, i):
    B = [0] * len(T)
    C = [0] * n

    for j in range( len(T) ):
        C[ change( T[j], n, i ) ] += 1
    #
    for j in range(1,n):
        C[ j ] = C[ j ] + C[ j - 1 ]
    #
    for j in range( len(T) - 1, -1, -1):
        B[ C[ change( T[j], n, i) ] - 1 ] = T[j]
        C[ change( T[j], n, i) ] -= 1
    #
    return B
#end def ^^^

def radixSort(T, n):
    #
    for i in range(1,3):
        T = countingSort(T,n,i)
    #
    return T
#end def ^^^

T = [15,3,6,4,16]
T = radixSort(T, 5)
print(T)

#
